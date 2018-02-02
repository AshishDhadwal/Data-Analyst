
# coding: utf-8

# In[1]:

def tag_count(list_strings):
    count = 0
    for item in list_strings:
        if item.startswith("<") and item.endswith(">"):
            count += 1
    return count
# Test for the tag_count function:
list1 = ['<greeting>', 'Hello World!', '</greeting>']
count = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(count))

