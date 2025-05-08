subjects = ["math","english","music","science"]
no_subjects = input(f"how many subjects out of this list: {subjects} do you want to pick?\n")
for subject in subjects[:int(no_subjects)]:
    print(subject)
