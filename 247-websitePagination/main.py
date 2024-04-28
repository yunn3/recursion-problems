def websitePagination(urls: int, pageSize: int, page: int) -> list[str]:
    urls_length = len(urls)
    first_url_index = pageSize * page - pageSize
    last_url_index = first_url_index + pageSize

    if not (pageSize * page <= urls_length):
        last_url_index = urls_length

    return urls[first_url_index:last_url_index]
