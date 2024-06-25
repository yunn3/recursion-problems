import markdown


def main() -> None:
    markdown_file_name = "sample.md"
    with open(markdown_file_name, "r", encoding="utf-8") as mdfile:
        text = mdfile.read()

        html = markdown.markdown(text)

    html_file_name = "index.html"
    with open(html_file_name, "w", encoding="utf-8") as html_file:
        html_file.write(html)


if __name__ == "__main__":
    main()
