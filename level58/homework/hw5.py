def search_substr(query, words):
    query_lower = query.lower()
    result = [word for word in words if query_lower in word.lower()]
    return result if result else ["None"]