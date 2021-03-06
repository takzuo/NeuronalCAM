import numpy as np

from data_prep import features,targets, features_test, targets_test

def sigmoide(x):
    return 1/(1 + np.exp(-x))


#Hyperparameters

n_hidden = 2
epochs = 1000
alpha = 0.05

m,k = features.shape # numero de ejemplos de entrenamiento, 

#inicializacion de los pesos
entrada_escondida = np.random.normal(scale = 1/k**0.5,
                                     size = (k,n_hidden)
                                    )
escondida_salida = np.random.normal(scale = 1/k**0.5,
                                    size = n_hidden
)

#entrenamiento

for e in range(epochs):

    #variables para el gradiente
    gradiente_entrada_escondida = np.zeros(entrada_escondida.shape)
    gradiente_escondida_salida = np.zeros(escondida_salida.shape)

    #Itera sobre el conjunto de entrenamiento

for x,y in zip(features.values, targets):
    #pasada hacia adelante (forward pass)

    z = sigmoide(np.matmul(x, entrada_escondida))
    y_ = sigmoide(np.matmul(escondida_salida, z)) # prediccion

    # Pasada hacia atras (backward pass)

    salida_error = (y - y_) * y_ *(1- y_)

    escondida_error = np.dot(salida_error, escondida_salida) * z * (1 -z)

    gradiente_entrada_escondida += escondida_error * x[:,None]
    gradiente_escondida_salida += salida_error * z

# Actualiza los parametros ( pesos)
entrada_escondida += alpha * gradiente_entrada_escondida / m
escondida_salida += alpha * gradiente_escondida_salida / m


if e % (epochs / 10 ) == 0:
    z = sigmoide(np.dot(features.values, entrada_escondida))
    y_ = sigmoide(np.dot(z, escondida_salida))

    #funcion de costo
    costo = np.mean(( y_ - targets)**2 )
    
    if ult_costo and ult_consto < costo:
        print("Costo de entrenamiento: ", costo, "Advertencia")
    else:
        print("consto de entrenamiento: ", costo )

    ult_consto = costo 

#precision en los datos de prueba
z = sigmoide(np.dot(features_test, entrada_escondida))
y_ = sigmoide(np.dot(z, escondida_salida))

predicciones = y_ > 0.5
precision = np.mean(predicciones == targets_test)
print("Precision: {:.3f}".format(precision))

 

