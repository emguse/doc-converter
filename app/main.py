from fastapi import FastAPI, HTTPException, BackgroundTasks, Query
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Literal
import subprocess
import os
import uuid
import tempfile

app = FastAPI()

class MarkdownInput(BaseModel):
    markdown: str

def cleanup_file(file_path: str):
    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Error removing file {file_path}: {e}")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/convert", summary="Markdown to PDF Converter", description="JSONで受け取ったMarkdownをPandocでPDFに変換して返します。")
async def convert_markdown(
    input: MarkdownInput,
    background_tasks: BackgroundTasks,
    orientation: Literal["portrait", "landscape"] = Query("portrait", description="用紙向き。portrait（縦）またはlandscape（横）")
):
    # システムの一時ディレクトリを利用し、一意なファイル名を生成
    temp_dir = tempfile.gettempdir()
    unique_id = str(uuid.uuid4())
    input_md = os.path.join(temp_dir, f"{unique_id}.md")
    output_pdf = os.path.join(temp_dir, f"{unique_id}.pdf")
    
    try:
        # Markdownテキストを一時ファイルに保存
        with open(input_md, "w", encoding="utf-8") as f:
            f.write(input.markdown)
        
        # Pandocのコマンドを組み立て
        pandoc_cmd = [
            "pandoc", input_md,
            "-o", output_pdf,
            "--pdf-engine=xelatex",
            "-V", "mainfont=Noto Sans CJK JP",
            "-V", "geometry:margin=1in",
            "--wrap=preserve"
        ]
        # 用紙向きが landscape の場合、geometry オプションを追加
        if orientation == "landscape":
            pandoc_cmd.extend(["-V", "geometry:landscape"])
        
        subprocess.run(pandoc_cmd, check=True)
        
        # 出力されたPDFが存在するか確認
        if not os.path.exists(output_pdf):
            raise HTTPException(status_code=500, detail="PDF出力ファイルが見つかりません。")
        
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail="変換に失敗しました。") from e
    finally:
        # Markdownファイルは不要なので削除
        if os.path.exists(input_md):
            os.remove(input_md)
    
    # レスポンス送信後にPDFファイルを削除するための BackgroundTask を追加
    background_tasks.add_task(cleanup_file, output_pdf)
    
    return FileResponse(output_pdf, media_type="application/pdf", filename="converted.pdf")