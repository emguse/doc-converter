import os
from fastapi.testclient import TestClient
import pytest

from app.main import app, MAX_MARKDOWN_LENGTH

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_convert_markdown_valid():
    # サンプルのMarkdownテキスト
    markdown_text = "# Sample Markdown\n\nThis is a test.\n\n- item1\n- item2"
    response = client.post("/convert", json={"markdown": markdown_text, "orientation": "portrait"})
    assert response.status_code == 200
    # Content-Type が PDF であることを確認
    assert response.headers["content-type"] == "application/pdf"
    # レスポンスの内容が空でないことを確認
    assert len(response.content) > 0

def test_convert_markdown_landscape():
    # 用紙向きが "landscape" の場合のテスト
    markdown_text = "# Landscape Test\n\nThis is a test for landscape orientation."
    response = client.post("/convert", json={"markdown": markdown_text, "orientation": "landscape"})
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"
    assert len(response.content) > 0

def test_convert_markdown_too_large():
    # 入力サイズが上限を超える場合のテスト
    markdown_text = "A" * (MAX_MARKDOWN_LENGTH + 1)
    response = client.post("/convert", json={"markdown": markdown_text})
    assert response.status_code == 413
    # エラーメッセージに「入力されたMarkdownのサイズが大きすぎます」が含まれることを確認
    assert "入力されたMarkdownのサイズが大きすぎます" in response.json()["detail"]