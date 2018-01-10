#! usr/bin/env python



def bubble(bubblelsit):
    lenth = len(bubblelsit)
    for i in range(lenth-1) :
        if bubblelsit[i+1]>bubblelsit[i]:
			bubblelsit[i],bubblelsit[i+1] = bubblelsit[i+1] ,bubblelsit[i]
		i+=1
	return bubblelsit

if __name__ == '__main__':

	quenue = raw_input('input a list:')
	bubblelsit = quenue.split()
	print bubble(bubblelsit)
