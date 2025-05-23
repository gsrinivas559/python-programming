# with --> using with function, we can open and close the file in one line
# By default, Python considers the file in reader mode
# with(filename, operation) --> operation is which mode we want to open the file.
# eg: read mode as 'r' and write mode as 'w'
# my scenario is fetch the content from the file
# reverse the content
# wire the reversed content in to the file
with open('languages.txt', 'r') as reader:
    # fetch the content from the file
    content = reader.readlines()  # ['Python', 'Java', 'Javascript', 'C#', 'Ruby']
    # In python, reversed function is present to reverse the content
    reversed(content)  # [Ruby, 'C#', 'Javascript', 'Java', 'Python']
    with open('languages.txt', 'w') as writer:
        for value in reversed(content):
            writer.write(value)
