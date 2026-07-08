keyword = input("Enter a keyword to search for in the post: ")
post = "Hi, my name is Pranay and I am a software developer. I love coding in Python and JavaScript. In my free time, I enjoy hiking and reading books."
if keyword in post:
    print(f"The keyword '{keyword}' is present in the post.")
else:
    print(f"The keyword '{keyword}' is not present in the post.")