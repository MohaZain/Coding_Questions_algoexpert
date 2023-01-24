def tournamentWinner(competitions, results):
    # Write your code here.
    dict_res = {}
    for idx,i in enumerate(results): 
        if i == 0:
            dict_res[competitions[idx][1]] = dict_res.get(competitions[idx][1],0) + 3
        else:
            dict_res[competitions[idx][0]] = dict_res.get(competitions[idx][0],0) + 3
    return max(dict_res, key=dict_res.get)



competitions_ = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]
results_ = [0,0,1]

print(tournamentWinner(competitions_,results_))