NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


# def dedup_and_title_case_names(names):
#     """Should return a list of title cased names,
#        each name appears only once"""
#     cleaned_names = []
#     for name in names:
#         if not (name in cleaned_names):
#             cleaned_names.append(name)
#     clean_and_title = []
#     for name in cleaned_names:
#         clean_and_title.append(name.title())
#     return clean_and_title


# def sort_by_surname_desc(names):
#     """Returns names list sorted desc by surname"""
#     names = dedup_and_title_case_names(names)
#     dic_names = []
#     for name in names:
#         first, last = name.split(' ')
#         dic_names.append({'first' : first, 'last': last})
#     def myfunc(arr):
#         return arr['last']
#     dic_names.sort(key = myfunc, reverse=True)
#     sorted_names = []
#     for ele in dic_names:
#         sorted_names.append(ele['first'] + ' '+ ele['last'])
#     return sorted_names


# def shortest_first_name(names):
#     """Returns the shortest first name (str).
#        You can assume there is only one shortest name.
#     """
#     names = dedup_and_title_case_names(names)
#     dic_names = []
#     for name in names:
#         first, last = name.split(' ')
#         dic_names.append({'first': first, 'last': last})
#     def myfunc(arr):
#         return len(arr['first'])
#     dic_names.sort(key=myfunc)
#     return dic_names[0]['first']

# **************************************************
# **************************************************
# ************* REFACTORING ************************
def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once """
    return [n.title() for n in set(names)]

def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names.sort(key=lambda x: x.split()[1], reverse=True)
    return names

def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    return min((n.split()[0] for n in names), key = len)




# *******************************************
# *******************************************
# ************* TEST ************************
