#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 20:09:17 2018

@author: haichunkan
"""

def merge_sort(A):
    merge_sort2(A,0,len(A)-1)
def merge_sort2(A,first,last):
    middle=(first+last)//2
    merge_sort2(A,first,middle)
    merge_sort2(A,middle+1,last)
    merge(A,first,middle+1,last)
def merge(A,first,middle,last):
    
    L=A[first:middle+1]
    R=A[middle+1:last+1] 
    L.append(9999999)
    R.append(9999999)
    i=j=0
    for k in range(first,last+1):
        if L[i]<=R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
A=[83,34,57,12,65,49,28,71]    
merge_sort(A) 
'''
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        #print ("L:",lefthalf,"R", righthalf,"All", alist)
        mergeSort(lefthalf)
        #print ("L:",lefthalf,"R", righthalf,"All", alist)
        mergeSort(righthalf)
        #print ("L:",lefthalf,"R", righthalf,"All", alist)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
'''       