#!/usr/bin/python3

my_story = "my name is {name}, i am a student in alx taking {course}"

name = input('what is your name: ')
course = input("what course do you do: ")

full_story = my_story.format(name=name, course=course)
print(full_story)