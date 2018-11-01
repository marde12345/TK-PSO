import numpy as np
import random as rand
import matplotlib.pyplot as plt

def main():
    #Variables
    n = 5
    num_variables = 2

    #Create Array
    a = np.empty((num_variables, n))
    v = np.empty((num_variables, n))
    Pbest = np.empty((num_variables, n))
    Gbest = np.empty((1, 2))
    r = np.empty((n))

    #Random Array
    for i in range(0, num_variables):
        for j in range(0, n):
            Pbest[i][j] = rand.randint(-10, 10)
            a[i][j] = Pbest[i][j]
            v[i][j] = 0
    
    #r
    for i in range(0, n):
        r[i] = fitness(a[0][i], a[1][i])

    #Sort Pbest
    Sort(Pbest, r, n)

    Gbest[0][0] = Pbest[0][0]
    Gbest[0][1] = Pbest[1][0]
    print('gbest ak ',Gbest)

    generation = 0

    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid(True)
    
    while(generation < 50):
        for i in range(n):
            #Pbest
            if(fitness(a[0][i], a[1][i]) < fitness(Pbest[0][i], Pbest[1][i])):
                Pbest[0][i] = a[0][i]
                Pbest[1][i] = a[1][i]
            #Gbest
            if(fitness(Pbest[0][i], Pbest[1][i]) < fitness(Gbest[0][0], Gbest[0][1])):
                Gbest[0][0] = Pbest[0][i]
                Gbest[0][1] = Pbest[1][i]
            #Velocity
            Vector_velocity(n, a, Pbest, Gbest, v)
        generation = generation + 1
        print ('Generation: ' + str(generation) + ' - - - Gbest: ' +str(Gbest))

        line1 = ax.plot(a[0], a[1], 'r+')
        line2 = ax.plot(Gbest[0][0], Gbest[0][1], 'g*')

        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        
        fig.canvas.draw()
        fig.savefig('./evol_conc_v'+str(generation)+'.png')
        ax.clear()
        ax.grid(True)

    plt.show()
    print ('Gbest: ')
    print (Gbest)

def Vector_velocity(n, a, Pbest, Gbest, v):
    for i in range(n):
        #X
        v[0][i] = 0.7 * v[0][i] + (Pbest[0][i] - a[0][i]) * rand.random() * 1.47 + (Gbest[0][0] - a[0][i]) * rand.random() * 1.47
        a[0][i] = a[0][i] + v[0][i]
        #Y
        v[1][i] = 0.7 * v[1][i] + (Pbest[1][i] - a[1][i]) * rand.random() * 1.47 + (Gbest[0][1] - a[1][i]) * rand.random() * 1.47
        a[1][i] = a[1][i] + v[1][i]

def fitness(x, y):
        return 100 * ((y - (x**2))**2) + ((1 - (x))**2)
        #100 * (y-x^2)^2+(1-x^2)^2

def Sort(Pbest, r, n):
    #Bubble Sort
    for i in range(1, n):
        for j in range(0, n - 1):
            if r[j] > r[j + 1]:
                #fitness
                tempRes = r[j]
                r[j] = r[j + 1]
                r[j + 1] = tempRes

                #X, Y
                tempX = Pbest[0][j]
                Pbest[0][j] = Pbest[0][j + 1]
                Pbest[0][j + 1] = tempX

                #Pbest
                tempY = Pbest[1][j]
                Pbest[1][j] = Pbest[1][j + 1]
                Pbest[1][j + 1] = tempY

main()