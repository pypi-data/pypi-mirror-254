import tkinter as tk
from tkinter import ttk
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import RidgeClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import BatchNormalization

class ml_model:
    def __init__(self,X,y,split=0.25,randomness=0,type=0):
        self.master = tk.Tk()
        self.master.geometry('300x300')
        self.master.configure(bg='#121212')
        self.master.resizable(False, False)
        self.type=type
        self.model=None
        self.X_train,self.X_test,self.y_train,self.y_test=train_test_split(X, y, test_size=split, random_state=randomness)
        self.master.title("ML MODEL BUILDER")
        if self.type==0:
            text='CHOOSE ALGORITHM FOR CLASSIFICATION'
        else:
            text='CHOOSE ALGORITHM FOR REGRESSION'
        self.label_top = tk.Label(self.master, text=text,font=("Arial", 10, "bold"),bg='#121212',fg='#FFFFFF')
        self.label_top.pack(pady=10)
        if self.type==0:
            options = ['Logistic Regression','k-Nearest Neighbors Classification','Support Vector Classification Linear','Support Vector Classification Non-Linear','Decision Trees Classification','Random Forest Classification','Naive Bayes','Ridge Classifier']#classification
        else:
            options = ['Linear Regression','Ridge Regression','Lasso Regression','Elastic Net','k-Nearest Neighbors Regression','Decision Tree Regressor','Random Forest Regressor','Support Vector Regression Linear','Support Vector Regression Non-Linear']#regression
        self.variable = tk.StringVar()
        self.variable.set("")
        self.menu = ttk.Combobox(self.master,width=40,background='gray' ,textvariable=self.variable, values=options)
        self.menu.pack(pady=30)
        self.button = tk.Button(self.master, text="ACCURACY",bg='#3498db',fg='#000000', font=("Arial", 11, "bold"),width=20,height=1,command=self.accuracy_value)
        self.button.pack(pady=10)
        self.accuracy_label = tk.Label(self.master, text="ACCURACY: ",font=("Arial", 11, "bold"),bg='#121212',fg='#FFFFFF')
        self.accuracy_label.pack(pady=20)
        
    def model_class(self,value):
        if value=='Random Forest Classification':
            model = RandomForestClassifier()
        elif value=='Support Vector Classification Linear':
            model=svm.SVC(kernel='linear')
        elif value=='Ridge Classifier':
            model = RidgeClassifier()
        elif value=='Support Vector Classification Non-Linear':
            model=svm.SVC(kernel='poly')
        elif value=='Logistic Regression':
            model = LogisticRegression()
        elif value=='k-Nearest Neighbors Classification':
            model = KNeighborsClassifier(n_neighbors=3)
        elif value=='Decision Trees Classification':
            model = DecisionTreeClassifier()
        elif value=='Naive Bayes':
            model = GaussianNB()#classification
        elif value=='Linear Regression':
            model = LinearRegression()
        elif value=='Ridge Regression':
            model = Ridge(alpha=1.0)
        elif value=='Lasso Regression':
            model = Lasso(alpha=0.1)
        elif value=='Elastic Net':
            model = ElasticNet(alpha=0.1, l1_ratio=0.5)
        elif value=='k-Nearest Neighbors Regression':
            model = KNeighborsRegressor(n_neighbors=3)
        elif value=='Decision Tree Regressor':
            model = DecisionTreeRegressor()
        elif value=='Random Forest Regressor':
            model = RandomForestRegressor(n_estimators=100)
        elif value=='Support Vector Regression Linear':
            model = SVR(kernel='linear')
        elif value=='Support Vector Regression Non-Linear':
            model = SVR(kernel='poly')
        model.fit(self.X_train,self.y_train)
        return model
    def model_selected(self):
        value = self.variable.get()
        self.model=self.model_class(value)
        self.master.destroy()
    def accuracy_value(self):
        value = self.variable.get()
        model=self.model_class(value)
        if self.type==0:
            accuracy=accuracy_score(self.y_test,model.predict(self.X_test))
        else:
            accuracy=r2_score(self.y_test,model.predict(self.X_test))
        self.accuracy_label.config(text=f"ACCURACY: {accuracy:.2f}")
    def algo(self):
        give_model = tk.Button(self.master, text="GIVE MODEL",bg='#3498db',fg='#000000', font=("Arial", 11, "bold"),width=15,height=1, command=self.model_selected)
        give_model.pack(pady=10)
        self.master.mainloop()


class clust_model:
    def __init__(self,X):
        self.root = tk.Tk()
        self.root.configure(bg='#121212')
        self.root.title("Clustering")
        self.X=X
        self.label = tk.Label(self.root, text="Enter number of clusters:",bg='#121212',fg='#FFFFFF',font=("Arial", 10, "bold"))
        self.label.pack(pady=10)
        self.model=None
        self.entry = ttk.Entry(self.root)
        self.entry.pack(pady=5)

        self.generate_button = tk.Button(self.root,bg='#3498db',fg='#000000', font=("Arial", 10, "bold"), text="Generate Scatter Plot",  command=self.generate_plot)
        self.generate_button.pack(pady=10)

        self.figure, self.ax = plt.subplots()
        self.ax.set_facecolor('#121212')
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack()
        self.label1 = tk.Label(self.root, text="Enter number of clusters:",bg='#121212',fg='#FFFFFF',font=("Arial", 10, "bold"))
        self.label1.pack(pady=10)
        self.entry1 = ttk.Entry(self.root)
        self.entry1.pack(pady=5)

    def get_model(self):
        input_size = self.entry1.get()
        try:
            input_size = int(input_size)
            if input_size <= 0:
                raise ValueError
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a positive integer for the list size.")
            return
        self.model = KMeans(n_clusters=input_size)
        self.model.fit(self.X)
        self.root.quit()

    def generate_plot(self):
        input_size = self.entry.get()
        try:
            input_size = int(input_size)
            if input_size <= 0:
                raise ValueError
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a positive integer for the list size.")
            return

        distortions = []
        inertias = []
        mapping1 = {}
        K = range(1,input_size+1)
 
        for k in K:
            kmeanModel = KMeans(n_clusters=k).fit(self.X)
            kmeanModel.fit(self.X)
 
            distortions.append(sum(np.min(cdist(self.X, kmeanModel.cluster_centers_,
                                        'euclidean'), axis=1)) / self.X.shape[0])
            inertias.append(kmeanModel.inertia_)
 
            mapping1[k] = sum(np.min(cdist(self.X, kmeanModel.cluster_centers_,
                                   'euclidean'), axis=1)) / self.X.shape[0]

        self.ax.clear()
        self.ax.plot(K, distortions, color='#FFFFFF', marker='x', linestyle='-')
        self.ax.set_xlabel("Index")
        self.ax.set_facecolor('#121212')
        self.ax.set_ylabel("Value")
        self.ax.set_title("Scatter Plot")

        self.canvas.draw()
    def clust(self):
        close_button = tk.Button(self.root,bg='#3498db',fg='#000000', text="MODEL", font=("Arial", 10, "bold") ,width=30,command=self.get_model)
        close_button.pack(pady=10)
        self.root.mainloop()

class dl_model:
    def __init__(self,X,y,split=0.25,randomness=0):
        self.root = tk.Tk()
        self.root.title("DL MODEL BUILDER")
        self.root.geometry("550x500")
        self.root.resizable(False, False)
        self.root.configure(bg='#121212')
        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.configure(bg='#121212')
        self.main_frame.pack(padx=10, pady=10)
        self.X_train,self.X_test,self.y_train,self.y_test=train_test_split(X, y, test_size=split, random_state=randomness)
        
        self.create_widgets()
        self.model=Sequential()
        self.rectangles = []
        self.first_rectangle = None
        self.root.mainloop()
        
    def create_widgets(self):
        label1 = tk.Label(self.main_frame, text="Layer",bg='#121212',fg='#FFFFFF',font=("Arial", 10, "bold"))
        label1.grid(row=0, column=0, padx=5, pady=5)
        
        label2 = tk.Label(self.main_frame, text="Activation Function",bg='#121212',fg='#FFFFFF',font=("Arial", 10, "bold"))
        label2.grid(row=0, column=1, padx=5, pady=5)
        
        label3 = tk.Label(self.main_frame, text="Value",bg='#121212',fg='#FFFFFF',font=("Arial", 10, "bold"))
        label3.grid(row=0, column=2, padx=5, pady=5)
        
        self.dropdown_var1 = tk.StringVar()
        self.dropdown_var2 = tk.StringVar()
        
        self.dropdown1 = ttk.Combobox(self.main_frame, textvariable=self.dropdown_var1)
        self.dropdown1['values'] = ['Fully Connected Layer', 'Dropout Layer', 'BatchNormalization Layer']
        self.dropdown1.grid(row=1, column=0, padx=5, pady=5)
        
        self.dropdown2 = ttk.Combobox(self.main_frame, textvariable=self.dropdown_var2)
        self.dropdown2['values'] = ['sigmoid', 'tanh', 'relu','softmax']
        self.dropdown2.grid(row=1, column=1, padx=5, pady=5)
        
        self.text_field = tk.Entry(self.main_frame)
        self.text_field.grid(row=1, column=2, padx=5, pady=5)
        
        self.add_button = tk.Button(self.main_frame, text='+', command=self.add_rectangle,bg='#3498db',fg='#000000',font=("Arial", 10, "bold"))
        self.add_button.grid(row=1, column=3, padx=5, pady=5)
        
        self.clear_button = tk.Button(self.main_frame, text='Clear', command=self.clear_rectangles,bg='#3498db',fg='#000000',font=("Arial", 10, "bold"))
        self.clear_button.grid(row=2, columnspan=4, padx=5, pady=5)
        
        self.frame = tk.Frame(self.root, width=400, height=400)
        self.frame.pack(padx=10, pady=10)
        
        self.canvas = tk.Canvas(self.frame, width=400, height=100)
        self.canvas.pack(side="left")
        
        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.inner_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        
        bottom_frame = tk.Frame(self.root)
        bottom_frame.configure(bg='#121212')
        bottom_frame.pack(padx=10, pady=10)
        
        label4 = tk.Label(bottom_frame, text="Optimizer",bg='#121212',fg='#FFFFFF',font=("Arial", 10, "bold"))
        label4.grid(row=0, column=0, padx=5, pady=5)
        
        label5 = tk.Label(bottom_frame, text="Loss",bg='#121212',fg='#FFFFFF',font=("Arial", 10, "bold"))
        label5.grid(row=0, column=1, padx=5, pady=5)
        
        
        self.dropdown_var3 = tk.StringVar()
        self.dropdown_var4 = tk.StringVar()
        
        self.dropdown3 = ttk.Combobox(bottom_frame, textvariable=self.dropdown_var3)
        self.dropdown3['values'] = ['Adam','Stochastic Gradient Descent', 'RMSProp ', 'Adagrad']
        self.dropdown3.grid(row=1, column=0, padx=5, pady=5)
        
        self.dropdown4 = ttk.Combobox(bottom_frame, textvariable=self.dropdown_var4)
        self.dropdown4['values'] = ['Mean Squared Error', 'Mean Absolute Error', 'Binary Cross-Entropy','Categorical Cross-Entropy','Sparse Categorical Cross-Entropy','Kullback-Leibler Divergence','Hinge','Huber','Poisson','Cosine Similarity']
        self.dropdown4.grid(row=1, column=1, padx=5, pady=5)
        
        label7 = tk.Label(bottom_frame, text="Epochs",bg='#121212',fg='#FFFFFF',font=("Arial", 10, "bold"))
        label7.grid(row=2, column=0, padx=5, pady=5)
        
        label8 = tk.Label(bottom_frame, text="Batch Size",bg='#121212',fg='#FFFFFF',font=("Arial", 10, "bold"))
        label8.grid(row=2, column=1, padx=5, pady=5)
        
        self.num_field1 = tk.Entry(bottom_frame)
        self.num_field1.grid(row=3, column=0, padx=5, pady=5)
        
        self.num_field2 = tk.Entry(bottom_frame)
        self.num_field2.grid(row=3, column=1, padx=5, pady=5)
        
        self.acc_button = tk.Button(bottom_frame, text='Process',command=self.acc_model,bg='#3498db',fg='#000000',font=("Arial", 10, "bold"))
        self.acc_button.grid(row=4, column=0, pady=20)
        
        self.acc_label = tk.Label(bottom_frame, text='Accuracy',bg='#121212',fg='#FFFFFF',font=("Arial", 10, "bold"))
        self.acc_label.grid(row=4, column=1, pady=20)
        
        self.close_button = tk.Button(bottom_frame, text='Model', command=self.root.destroy,bg='#3498db',fg='#000000',font=("Arial", 10, "bold"))
        self.close_button.grid(row=5, columnspan=3, padx=5, pady=10)
        
    
    
    def add_rectangle(self):
        option1 = str(self.dropdown_var1.get())
        option2 = str(self.dropdown_var2.get())
        text = self.text_field.get()
        
        if option1 and text and text.isdigit:
            rectangle_frame = tk.Frame(self.inner_frame)
            rectangle_frame.pack()
            
            label_text = f"{option1} - {option2} - {text}"
            label = tk.Label(rectangle_frame, text=label_text,fg='#121212',font=("Arial", 10, "bold"))
            label.pack(side="left", padx=5)
            
            if not self.first_rectangle:
                if option1=='Fully Connected Layer':
                    self.model.add(Dense(text, activation=option2,input_shape=(self.X_train.shape[1],)))#---------------------------------
                elif option1=='Dropout Layer':
                    self.model.add(Dropout(rate=text,input_shape=(self.X_train.shape[1],)))
                elif option1=='BatchNormalization Laycleer':
                    self.model.add(BatchNormalization(input_shape=(self.X_train.shape[1],)))
                self.first_rectangle = rectangle_frame
            else:
                if option1=='Fully Connected Layer':
                    self.model.add(Dense(text, activation=option2))
                elif option1=='Dropout Layer':
                    self.model.add(Dropout(text))
                elif option1=='BatchNormalization Layer':
                    self.model.add(BatchNormalization())
            self.rectangles.append(rectangle_frame)
            self.update_canvas_scrollregion()
         
        
    def clear_rectangles(self):
        for rectangle_frame in self.rectangles:
            rectangle_frame.pack_forget()
        self.rectangles = []
        if self.first_rectangle:
            self.first_rectangle.destroy()
            self.first_rectangle = None
        self.model=Sequential()
        self.update_canvas_scrollregion()
        
    def update_canvas_scrollregion(self):
        self.inner_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def compiling(self):
        opt=self.dropdown_var3.get()
        loss=self.dropdown_var4.get()
        if opt and loss:
            if opt=='Adam':
                opt='adam'
            elif opt=='Stochastic Gradient Descent':
                opt='sgd'
            elif opt=='RMSProp ':
                opt='rmsprop'
            elif opt=='Adagrad':
                opt='adagrad'
            if loss=='Mean Squared Error':
                loss='mean_squared_error'
            elif loss=='Mean Absolute Error':
                loss='mean_absolute_error'
            elif loss=='Binary Cross-Entropy':
                loss='binary_crossentropy'
            elif loss=='Categorical Cross-Entropy':
                loss='categorical_crossentropy'
            elif loss=='Sparse Categorical Cross-Entropy':
                loss='sparse_categorical_crossentropy'
            elif loss=='Kullback-Leibler Divergence':
                loss='kullback_leibler_divergence'
            elif loss=='Hinge':
                loss='hinge'
            elif loss=='Huber':
                loss='huber_loss'
            elif loss=='Poisson':
                loss='poisson'
            elif loss=='Cosine Similarity':
                loss='cosine_similarity'
        if opt and loss:
            self.model.compile(optimizer=opt, loss=loss, metrics=['accuracy'])

    
    def acc_model(self):
        self.compiling()
        epoch=int(self.num_field1.get())
        batch_size=int(self.num_field2.get())
        self.model.fit(self.X_train, self.y_train, batch_size=batch_size, epochs=epoch)
        loss, accuracy = self.model.evaluate(self.X_test, self.y_test)
        self.acc_label.config(text=f"Accuracy: {accuracy:.2f}")


class model_check:
    def __init__(self, model_list,X,y,type=0):
        if type<=0:
            type=0
        else:
            type=1
        self.type=type
        self.X=X
        self.y=y
        self.model_list = model_list
        self.root = tk.Tk()
        self.root.geometry('800x700')
        self.root.configure(bg='#121212')
        self.root.resizable(False, False)
        self.root.title("Model Check")
        
        self.button = tk.Button(self.root, text="Check", command=self.generate_graph,bg='#3498db',fg='#000000',font=("Arial", 11, "bold"))
        self.button.pack(pady=10)
        
        self.graph_frame = ttk.Frame(self.root)
        self.graph_frame.pack(fill=tk.BOTH, expand=True)
        self.convert_button = tk.Button(self.root, text="Close",bg='#3498db',fg='#000000',font=("Arial", 11, "bold"), command=self.close_window)
        self.convert_button.pack(pady=10)
        self.root.mainloop()
    
    def close_window(self):
        self.root.quit()
    
    def acc_models(self):
        acc_list=[]
        if self.type==0:
            for i in self.model_list:
                y_pred = i.predict(self.X)
                accuracy = accuracy_score(self.y, y_pred)
                acc_list.append(accuracy)
        else:
            for i in self.model_list:
                y_pred = i.predict(self.X)
                accuracy = r2_score(self.y, y_pred)
                acc_list.append(accuracy)
        return acc_list


    def generate_graph(self):
        plt.clf()
        data = self.acc_models()
        x_values = list(range(1, len(data) + 1))
        
        plt.bar(x_values, data)
        plt.xlabel("Model index")
        plt.ylabel("Accuracy")
        
        figure = plt.gcf()
        self.bar_graph = FigureCanvasTkAgg(figure, self.graph_frame)
        self.bar_graph.get_tk_widget().pack(fill=tk.BOTH, expand=True)
