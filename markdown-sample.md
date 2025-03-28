# This is Markdown

- one
- two
- three

## table sample

| one | two | three |
| --- | --- | ----- |
| 1 | 2 | 3 |

---

## 日本語サンプル

これは日本語です。
空行で一行空けるかダブルスペースがないと改行しません。

空行があると改行します(段落)。行末にダブルスペースも改行します（改行）。  
これは改行しているはずです。

## コードブロックのシンタクッスハイライト

```python
def main():
    print("Hello. World!!")

if __name__ == "__main__":
    main()
```

## mermaid.jsのチャートに対応する

```mermaid
graph TD
  A[doc-converter (Project Root)]
  A --> B[.devcontainer]
  B --> B1[Dockerfile]
  B --> B2[devcontainer.json]
  B --> B3[docker-compose.yml]
  A --> C[app]
  C --> C1[main.py]
  A --> D[pyproject.toml]
  A --> E[uv.lock]
```

## テスト用JSON

```json
{
  "markdown": "# This is Markdown\\n\\n- one\\n- two\\n- three\\n\\n## table sample\\n\\n| one | two | three |\\n| --- | --- | ----- |\\n| 1 | 2 | 3 |\\n\\n---\\n\\n## 日本語サンプル\\n\\nこれは日本語です。\\n空行で一行空けるかダブルスペースがないと改行しません。\\n\\n空行があると改行します(段落)。行末にダブルスペースも改行します（改行）。  \\nこれは改行しているはずです。\\n\\n## コードブロックのシンタクッスハイライト\\n\\n```python\\ndef main():\\n    print(\\\"Hello. World!!\\\")\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n```\\n\\n## mermaid.jsのチャートに対応する\\n\\n```mermaid\\ngraph TD\\n  A[doc-converter (Project Root)]\\n  A --> B[.devcontainer]\\n  B --> B1[Dockerfile]\\n  B --> B2[devcontainer.json]\\n  B --> B3[docker-compose.yml]\\n  A --> C[app]\\n  C --> C1[main.py]\\n  A --> D[pyproject.toml]\\n  A --> E[uv.lock]\\n```"
}
```
