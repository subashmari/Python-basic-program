import wikipedia

# Prompt the user to enter the name of the Wikipedia article to retrieve
article_name = input("Enter the name of the Wikipedia article to retrieve: ")

# Retrieve the Wikipedia page object for the specified article
article = wikipedia.page(article_name)

# Print the content of the article line by line
print(f"Content of '{article.title}':")
for line in article.content.splitlines():
    print(line)
