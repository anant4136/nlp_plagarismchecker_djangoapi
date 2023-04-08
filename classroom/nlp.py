# import os
from docx import Document

import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def check_plagiarism(data, plag):
    # read all the docx files in the given folder path
    path = '''C:/Users/Rog/OneDrive/Desktop/ml practical/project_api/plagiarism_classroom/paper/'''
    doc_files = data
    num_docs = len(doc_files)
    if num_docs < 2:
        return "Not enough documents to compare for plagiarism."

    # create a list of document texts
    docs = []
    for file in doc_files:
        f_name = file.split('/')[-1]
        document = Document(path+f_name)
        full_text = []
        for para in document.paragraphs:
            full_text.append(para.text)
        doc_text = '\n'.join(full_text)
        docs.append(doc_text)

    # vectorize the document texts and calculate cosine similarity between them
    vectorizer = TfidfVectorizer(stop_words='english')
    doc_vectors = vectorizer.fit_transform(docs)
    similarities = cosine_similarity(doc_vectors)

    # check plagiarism for each pair of documents
    results = []

    for i in range(num_docs):
        count = 0
        for j in range(i+1, num_docs):
            similarity = similarities[i][j]
            count += similarity
            if similarity > 0.8:
                result = f"Plagiarism detected between {doc_files[i]} and {doc_files[j]} with similarity {similarity:.2f}"
            else:
                result = f"No plagiarism detected between {doc_files[i]} and {doc_files[j]} with similarity {similarity:.2f}"
            results.append(result)
        plag.append(count)

    return results


# for result in results:
#     print(result)

# documents = ['Document 1', 'Document 2', 'Document 3', 'Document 4', 'Document 5']
# plagiarism = [10, 25, 50, 75, 90]

# # Plot the graph
# plt.plot(documents, plag)
# plt.title('Plagiarism in Documents')
# plt.xlabel('Document')
# plt.ylabel('Plagiarism (%)')
# plt.show()

# values = [1, 3, 2, 5, 4]

# Create a bar chart
# plt.bar(range(len(plag)), plag)

# # Add x-axis labels
# plt.xticks(range(len(plag)), documents)

# # Add y-axis label
# plt.ylabel('Value')

# # Add plot title
# plt.title('Bar chart example')

# # Display the plot
# plt.show()
