def origanize_hashtags(hashtags):
    unique_hashtags = set(hashtags)
    sorted_hashtags = sorted(unique_hashtags)
    return  sorted_hashtags

hashtags = input("Enter hashtags separated by Spaces: ").split()

origanized_hashtag= origanize_hashtags(hashtags)
print("\nOrganized hashtags")
for tag in origanized_hashtag:
    print("#" + tag)


