def search_book_isbn(isbn_list, target_isbn):
    left = 0
    right = len(isbn_list) - 1
    
    while left < right:
        middle = (left + right) // 2
        if isbn_list[middle] == target_isbn:
            return middle

        if target_isbn > isbn_list[middle]:
            left = middle + 1
        else:
            right = middle - 1

    if isbn_list[left] == target_isbn:
        return left
    return -1