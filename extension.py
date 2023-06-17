"""
File: extension.py
------------------
This is a file for creating an optional extension program, if
you'd like to do so. For the server extension, write your code in
extension_server.py
"""
#from searchengine import parse

def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    #index_ranking = get_index_ranking(all_document_lines)
    #ranking = {}
    pass

def sort_by_ranking(query, query_results, ranking, all_document_lines):
    rank = {}
    for filename in query_results:
        get_ranking_document(ranking, filename, all_document_lines)
        for word in query:
            if filename not in rank:
                rank[filename] = 0
            rank[filename] += ranking[filename][word]
    return dict(sorted(rank.items(), reverse=True))

def get_ranking_document(ranking, filename, all_document_lines):
    ranking[filename] = {}
    document_terms = parse(document_lines)
    for term in document_terms:
        if term not in ranking[filename]:
            ranking[filename][term] = 1
        else:
            ranking[filename][term] += 1

def parse(document_lines):
    document_terms = []
    for raw in document_lines.split():
        term = get_terms_lowercase(raw)
        if term != '':
            document_terms.append(term)
    return document_terms






# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
