
def print_movie():
    f = open('assets/filme.txt', 'r')
    file_contents = f.read()
    print (file_contents)
    f.close()
    