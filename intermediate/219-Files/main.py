class Files:

    def __init__(
        self, fileName: str, fileExtension: str, content: str, parentFolder: str
    ) -> None:

        self.fileName = fileName
        self.fileExtension = fileExtension
        self.content = content
        self.parentFolder = parentFolder

    def getLifetimeBandwidthSize(self) -> str:

        MB_file_size_per_character = 25
        number_of_character = len(self.content)
        MB_file_size = number_of_character * MB_file_size_per_character

        # MB_file_sizeが1000以上である場合は適切な位置に"."をつけてGB表記。以下である場合はそのままMB表記で返す。
        if MB_file_size >= 1000:
            return str(MB_file_size // 1000) + "." + str(MB_file_size % 1000) + "GB"

        return str(MB_file_size) + "MB"

    def prependContent(self, data: str) -> str:
        self.content = data + self.content
        return self.content

    def addContent(self, data: str, position: int) -> str:
        self.content = self.content[:position] + data + self.content[position:]
        return self.content

    def showFileLocation(self) -> str:
        return self.parentFolder + " > " + self.fileName + self.fileExtension


assignment = Files("assignment", ".word", "ABCDEFGH", "homework")
blade = Files(
    "blade",
    ".txt",
    "bg-primary text-white m-0 p-0 d-flex justify-content-center",
    "view",
)

print(assignment.getLifetimeBandwidthSize())
print(assignment.prependContent("MMM"))
print(assignment.addContent("hello world", 5))
print(assignment.showFileLocation())

print(blade.getLifetimeBandwidthSize())
print(
    blade.addContent(
        "font-weight-bold ",
        11,
    ),
)
print(blade.showFileLocation())
