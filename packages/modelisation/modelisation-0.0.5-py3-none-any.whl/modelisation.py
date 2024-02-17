# bibliothèque pour modéliser des graphiques : Stéphane LAURENT

import matplotlib.pyplot as plt # importation d'un sous module (pyplot) de la bibliothèque matplotlib sous le nom plt
import numpy as np # Importation du module numpy afin de lire le contenu du fichier csv
from scipy.optimize import curve_fit
from matplotlib.path import Path
from matplotlib.widgets import LassoSelector
from matplotlib.widgets import Cursor    # pour afficher un réticule
import addcopyfighandler				 # pour copier la graphique dans le presse papier avec ctrl C
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import warnings


#### Barre de navigation ####

NavigationToolbar2Tk.toolitems = (
    ('Home', "Réinitialiser la vue d'origine", 'home', 'home'),
    ('Back', 'Retour à la vue précédente', 'back', 'back'),
    ('Forward', 'Passer à la vue suivante', 'forward', 'forward'),
    (None, None, None, None),
    ('Pan', 'Clic gauche : déplacer le graphique\nClic droit : dilater/compresser le graphique', 'move', 'pan'),
    ('Zoom', 'Zoomer sur un rectangle', 'zoom_to_rect', 'zoom'),
    (None, None, None, None),
    ('Save', 'Enregistrer le graphique', 'filesave', 'save_figure'),
    )


# Variables globales
points_modelisation = []


def onSelect(points_lasso):
    global tableau_points
    global ind
    global message_erreur
    
    try:
        message_erreur.remove()
    except:
        pass
    
    ind = []
    path = Path(points_lasso)
    ind = np.nonzero(path.contains_points(tableau_points))[0]
    canvas.draw_idle()
    modelisation_points_lasso()


def selection_lasso(x1, y1):
    global tableau_points
    global lasso
      
    # mettre les points du graphique en tableau Numpy [[x1 y1] [x2 y2]...]
    tableau_points = []
    l2 = []
    for i in range(len(x1)):
        l1 = []
        l1.append(x1[i])
        l1.append(y1[i])
        l2.append(l1)
    
    tableau_points = np.asarray(l2)   
    lasso = LassoSelector(ax=plt.gca(), onselect=onSelect, props = {'color' : 'red', 'linewidth': 1.5, 'alpha': 0.8})
    
  
def effacer_modelisation():
    global legende
    global modele_choisi
    global points_modelisation
    global nbr_modelisation
    global titre_legende
    # effacer la modélisation précédente si elle existe
    
    try:     
        a_supprimer = points_modelisation.pop() # supprimer la dernière droite affichée
        a_supprimer.pop().remove()
        
        legende.remove()
        
        if modele_choisi == "double_affine" and nbr_modelisation >= 1: # afficher la legende de la première droite
            nbr_modelisation -=1
            plt.gca().legend(handles=points_modelisation[0])
            legende = plt.legend(loc = 'upper left', title = titre_legende, title_fontsize='large')
            legende._legend_box.align = "left"
    except:
        pass
    
    plt.gcf().canvas.draw()


def modelisation_points_lasso():
    
    global points_modelisation
    global legende
    global ind
    global x_points
    global y_points
    global modele_choisi
    global nbr_modelisation
    
    xx = []
    yy = []
    
    for i in range(len(ind)):
        xx.append(x_points[ind[i]])
        yy.append(y_points[ind[i]])
       
    if len(xx) > 1: # il faut au moins deux points pour modéliser
        
        if modele_choisi != "double_affine":
            effacer_modelisation()
        
        if modele_choisi == "lineaire" or modele_choisi == "linéaire":
            afficher_modele_lineaire(xx, yy)
        
        if modele_choisi == "affine" :
            afficher_modele_affine(xx, yy)
        
        if modele_choisi == "parabole" :
            afficher_modele_parabole(xx, yy)
            
        if modele_choisi == "exp_decroissante" :
            afficher_modele_exp_decroissante(xx, yy)
            
        if modele_choisi == "exp_croissante" :
            afficher_modele_exp_croissante(xx, yy)
        
        if modele_choisi == "double_affine" :
            
            if nbr_modelisation < 2:
                nbr_modelisation +=1
                afficher_modele_affine(xx, yy)
                
            if nbr_modelisation == 2:
                nbr_modelisation +=1
                effacer_modelisation()
                afficher_modele_affine(xx, yy)
            
    return



def touche_clavier(event):
            
    if event.key == "delete":
        effacer_modelisation()
        global message_erreur
    
        try:
            message_erreur.remove()
            plt.gcf().canvas.draw()
        except:
            pass
    
     #--------- Afficher / masquer un réticule libre ----------
    if event.key == "r":
        
        if reticule.visible == False:           
            reticule.visible = True
            
        else:
            reticule.visible = False
        
        
        plt.gcf().canvas.draw()
       
        
            

def affichage_message_erreur():
    global message_erreur
    message_erreur=plt.figtext(0.6, 0.5, 'Modélisation impossible !',fontsize = 16, fontweight = 'bold', color = 'red', backgroundcolor = 'yellow',horizontalalignment = 'center', verticalalignment = 'center')
        

### Modélisation ###

def lineaire(x, a):
    return a * x

def affine(x, a, b):
    return a * x + b

def parabole(x, a, b, c):
    return a * x**2 + b*x + c

def exp_decroissante(x, a, b):
    return a * np.exp(-b * x)

def exp_croissante(x, a, b):
    return a * (1 - np.exp(-b * x)) 


def afficher_modelisation(x_modelisation, y_modelisation, titre_legende, caracteristiques_modele):
    global points_modelisation
    global legende
    global modele_choisi
    global nbr_modelisation
    
    if modele_choisi == "double_affine" and nbr_modelisation > 1:
        couleur = "green"
    else:
        couleur = "blue"
        
    points_modelisation.append(plt.plot(x_modelisation, y_modelisation, color=couleur, linestyle='solid', linewidth=1.5, label = caracteristiques_modele))
    
    legende = plt.legend(loc = 'upper left', title = titre_legende, title_fontsize='large')
    legende._legend_box.align = "left"
    
    
        
def afficher_modele_affine(x1, y1):
    global titre_legende
    
    try:
        popt,pcov = curve_fit(affine, x1, y1) 
        a = popt[0]
        b = popt[1]
        
        xmin, xmax = plt.gca().xaxis.get_view_interval() # valeurs extrêmes sur l'axe des x
        x_modelisation = np.linspace(xmin, xmax)
        y_modelisation = a * x_modelisation + b
              
        titre_legende = '$\\bf{y = a\/x + b}$'
        caracteristiques_modele = "a = " + "{0:.3g}".format(a) + "\nb = " + "{0:.3g}".format(b)
        afficher_modelisation(x_modelisation, y_modelisation, titre_legende, caracteristiques_modele)
    except:
         affichage_message_erreur()
    return


def afficher_modele_lineaire(x1,y1):
    try:
        popt,pcov = curve_fit(lineaire, x1, y1) 
        a = popt[0]
        
        xmin, xmax = plt.gca().xaxis.get_view_interval() # valeurs extrêmes sur l'axe des x
        x_modelisation = np.linspace(0, xmax)
        y_modelisation = a * x_modelisation
        
        titre_legende = '$\\bf{y = a\/x}$'
        caracteristiques_modele = "a = " + "{0:.3g}".format(a)
        afficher_modelisation(x_modelisation, y_modelisation, titre_legende, caracteristiques_modele)
    except:
        affichage_message_erreur()
    return


def afficher_modele_parabole(x1, y1):               
    try:
        popt,pcov = curve_fit(parabole, x1, y1) 
        a = popt[0]
        b = popt[1]
        c = popt[2]
        
        xmin, xmax = plt.gca().xaxis.get_view_interval() # valeurs extrêmes sur l'axe des x
        x_modelisation = np.linspace(xmin, xmax)
        y_modelisation = a * x_modelisation**2 + b * x_modelisation + c
        
        titre_legende = '$\\bf{y = a\/x² + b\/x + c}$'
        caracteristiques_modele = "a = " + "{0:.3g}".format(a) + "\nb = " + "{0:.3g}".format(b) + "\nc = " + "{0:.3g}".format(c)
        afficher_modelisation(x_modelisation, y_modelisation, titre_legende, caracteristiques_modele)
    except:
        affichage_message_erreur()
    return


def afficher_modele_exp_decroissante(x1, y1):       
    try:
        popt,pcov = curve_fit(exp_decroissante, x1, y1) 
        a = popt[0]
        b = popt[1]
        
        xmin, xmax = plt.gca().xaxis.get_view_interval() # valeurs extrêmes sur l'axe des x
        x_modelisation = np.linspace(xmin, xmax)
        y_modelisation = a * np.exp(-b * x_modelisation)
        
        titre_legende = '$\\bf{y = a\/\/exp(-bx )}$'
        caracteristiques_modele = "a = " + "{0:.3g}".format(a) + "\nb = " + "{0:.3g}".format(b)
        afficher_modelisation(x_modelisation, y_modelisation, titre_legende, caracteristiques_modele)
    except:
        affichage_message_erreur()
    return


def afficher_modele_exp_croissante(x1, y1):
    try:
        popt,pcov = curve_fit(exp_croissante, x1, y1) 
        a = popt[0]
        b = popt[1]
        
        xmin, xmax = plt.gca().xaxis.get_view_interval() # valeurs extrêmes sur l'axe des x
        x_modelisation = np.linspace(xmin, xmax)
        y_modelisation = a * (1 - np.exp(-b * x_modelisation)) 
        
        titre_legende = '$\\bf{y = a\/\/(1 - exp(-bx))}$'
        caracteristiques_modele = "a = " + "{0:.3g}".format(a) + "\nb = " + "{0:.3g}".format(b)
        afficher_modelisation(x_modelisation, y_modelisation, titre_legende, caracteristiques_modele)
    except:
        affichage_message_erreur()
    return


def modele(modele, x1, y1):
    
    global x_points
    global y_points
    global modele_choisi
    global points_modelisation
    global canvas
    
    canvas = plt.gca().figure.canvas
    
    plt.gcf().canvas.mpl_connect("key_press_event", touche_clavier)
    
    x_points = x1
    y_points = y1
    
    if modele.lower() == "double-affine":
        modele = "double_affine"
        
    modele_choisi = modele.lower()
    
    xmin, xmax = plt.gca().xaxis.get_view_interval() # valeurs extrêmes sur l'axe des x
    
    if modele_choisi == "lineaire" or modele_choisi == "linéaire":
        afficher_modele_lineaire(x_points, y_points)
        selection_lasso(x_points, y_points)        
        return 
        
    if modele_choisi == "affine":
        afficher_modele_affine(x_points, y_points)
        selection_lasso(x_points, y_points)              
        return
    
    
    if modele_choisi == "parabole":
        afficher_modele_parabole(x_points, y_points)
        selection_lasso(x_points, y_points)
        return
    
    if modele_choisi == "exp_decroissante" or modele_choisi == "exp-decroissante":
        afficher_modele_exp_decroissante(x_points, y_points)
        selection_lasso(x_points, y_points)
        return
        
    
    if modele_choisi == "exp_croissante" or modele_choisi == "exp-croissante":
        afficher_modele_exp_croissante(x_points, y_points)
        selection_lasso(x_points, y_points)
        return 
    
    if modele_choisi == "double_affine":
        global nbr_modelisation # nombre de droite modélisées pour "double_affine"
        nbr_modelisation = 0
        selection_lasso(x_points, y_points)

reticule = Cursor(plt.gca(), useblit=True, color='black', linewidth=1, linestyle='dashed')
reticule.visible = False

warnings.filterwarnings(action='ignore') # empêcher l'affichage d'avertissement Python

