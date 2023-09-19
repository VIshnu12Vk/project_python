from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
import numpy as np
import pandas as pd
from kivymd.toast import  toast

KV = """

ScreenManager:
    MenuScreen:  
<MenuScreen>
    
    name: 'menu'
    id: mnu
    
    MDGridLayout:
        padding: "20dp"
        cols: 2
        
        MDCard:
            
            md_bg_color: 1,1,1, 1
            orientation: "vertical"
            padding: "10dp"
            MDGridLayout:
                padding: "20dp"
                cols: 1
                MDLabel:
                    text: "MLDOCTOR"
                    halign: "center"
                    md_bg_color:244/255,243/255,251/255, 1
                    size_hint_y: None
                    height: self.texture_size[1]  
                    font_size: "20sp"
                MDSeparator:
                    height: "10dp"
                    md_bg_color: 1,1,1, 1  
                MDLabel:
                    text: "A Machine Learning Approach to Predict Human Diseases "
                    halign: "center"
                    md_bg_color:244/255,243/255,251/255, 1
                    size_hint_y: None
                    height: self.texture_size[1]  
                    font_size: "15sp"
                MDSeparator:
                    height: "120dp"
                    md_bg_color: 1,1,1, 1  
                
                MDRaisedButton:
                    id: button1
                    icon: "bug"
                    text: "none "
                    md_bg_color:167/255,153/255,255/255, 1
                    on_release: app.dropdown1.open()
                    padding: "20dp"
                MDSeparator:
                    height: "10dp"
                    md_bg_color: 1,1,1, 1
                MDRaisedButton:
                    id: button2
                    icon: "bug"
                    text: "none"
                    md_bg_color:167/255,153/255,255/255, 1
                    on_release: app.dropdown2.open()
                    padding: "20dp"
                MDSeparator:
                    height: "10dp"
                    md_bg_color: 1,1,1, 1
                MDRaisedButton:
                    id: button3
                    icon: "bug"
                    text: "none"
                    md_bg_color:167/255,153/255,255/255, 1
                    on_release: app.dropdown3.open()
                    padding: "20dp"
                MDSeparator:
                    height: "10dp"
                    md_bg_color: 1,1,1, 1
                MDRaisedButton:
                    id: button4
                    icon: "bug"
                    text: "none"
                    md_bg_color:167/255,153/255,255/255, 1
                    on_release: app.dropdown4.open()
                MDSeparator:
                    height: "10dp"
                    md_bg_color: 1,1,1, 1
                   
                MDRaisedButton:
                    id: button5
                    icon: "bug"
                    text: "none"
                    on_release: app.dropdown5.open()
                    md_bg_color:167/255,153/255,255/255, 1
                    padding: "20dp"
                
                
                
                
                    
                    
            
        MDCard:
            
            md_bg_color: 244/255,243/255,251/255, 1
            orientation: "vertical"
            padding: "10dp"
            MDGridLayout:
                padding: "20dp"
                cols: 1
                MDTextField:
                    id: t1
                    hint_text: "Test 1 Result"
                MDSeparator:
                    height: "10dp"
                    md_bg_color: 244/255,243/255,251/255, 1
                MDTextField:
                    id: t2
                    hint_text: "Test 2 Result"
                    
                MDSeparator:
                    height: "10dp"
                    md_bg_color: 244/255,243/255,251/255, 1
                MDTextField:
                    id: t3
                    hint_text: "Test 3 Result"
                MDSeparator:
                    height: "10dp"
                    md_bg_color: 244/255,243/255,251/255, 1
                MDRaisedButton:
                    icon: "test-tube"
                    text: "Test1"
                    on_press: app.Testing(1)
                    md_bg_color:167/255,153/255,255/255, 1
                    padding: "20dp"
                MDSeparator:
                    height: "10dp"
                    md_bg_color: 244/255,243/255,251/255, 1
                MDRaisedButton:
                    icon: "test-tube"
                    text: "Test2"
                    on_press: app.Testing(2)
                    md_bg_color:167/255,153/255,255/255, 1
                    padding: "20dp"
                MDSeparator:
                    height: "10dp"
                    md_bg_color: 244/255,243/255,251/255, 1
                MDRaisedButton:
                    icon: "test-tube"
                    text: "Test3"
                    on_press: app.Testing(3)
                    md_bg_color:167/255,153/255,255/255, 1
                    padding: "20dp"
                MDSeparator:
                    height: "10dp"
                    md_bg_color: 244/255,243/255,251/255, 1
                MDRaisedButton:
                    text: "Clear"
                    text_color: 167/255,153/255,255/255, 1
                    on_press: app.clear_text()
                    md_bg_color: 1,1,1,1
                    padding: "20dp"
                MDSeparator:
                    height: "10dp"
                    md_bg_color: 244/255,243/255,251/255, 1
                MDRaisedButton:
                    text: "Exit"
                    text_color: 167/255,153/255,255/255, 1
                    on_press: app.get_running_app().stop()
                    md_bg_color: 1,1,1,1
                    padding: "20dp"
                MDSeparator:
                    height: "30dp"
                    md_bg_color: 244/255,243/255,251/255, 1
                MDLabel:
                    text: "tips : consider the average result of 3 test!"
                    halign: "center"
                    md_bg_color: 1,1,1,1
                    size_hint_y: None
                    height: self.texture_size[1]  
                    font_size: "13sp"
                MDSeparator:
                    height: "10dp"
                    md_bg_color: 244/255,243/255,251/255, 1
                MDLabel:
                    text: "MLDOCTOR"
                    halign: "center"
                    md_bg_color: 1,1,1,1
                    size_hint_y: None
                    height: self.texture_size[1]  
                    font_size: "20sp"




"""


class MenuScreen(Screen):
    pass



sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))

class MlDoctor(MDApp):

    l1 = ['back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
          'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
          'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
          'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
          'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
          'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
          'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
          'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
          'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
          'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
          'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
          'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
          'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
          'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria',
          'family_history', 'mucoid_sputum',
          'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
          'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
          'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf',
          'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
          'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
          'yellow_crust_ooze']
    disease = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
               'Peptic ulcer diseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',
               ' Migraine', 'Cervical spondylosis',
               'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid',
               'hepatitis A',
               'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis',
               'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
               'Heartattack', 'Varicoseveins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia',
               'Osteoarthristis',
               'Arthritis', '(vertigo) Paroxysmal  Positional Vertigo', 'Acne', 'Urinary tract infection',
               'Psoriasis',
               'Impetigo']
    l2 = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        for x in range(0, len(self.l1)):
            self.l2.append(0)
        self.l1.sort()
        menu_items_button = [
            {
                "viewclass": "OneLineListItem",
                "text": i,
                "on_press": lambda o=i: self.menu_callback(o, 1)

            } for i in self.l1

        ]
        menu_items_button2 = [
            {
                "viewclass": "OneLineListItem",
                "text": i,
                "on_press": lambda o=i: self.menu_callback(o, 2)

            } for i in self.l1

        ]
        menu_items_button3 = [
            {
                "viewclass": "OneLineListItem",
                "text": i,
                "on_press": lambda o=i: self.menu_callback(o, 3)

            } for i in self.l1

        ]
        menu_items_button4 = [
            {
                "viewclass": "OneLineListItem",
                "text": i,
                "on_press": lambda o=i: self.menu_callback(o, 4)

            } for i in self.l1

        ]
        menu_items_button5 = [
            {
                "viewclass": "OneLineListItem",
                "text": i,
                "on_press": lambda o=i: self.menu_callback(o, 5)

            } for i in self.l1

        ]

        self.dropdown1 = MDDropdownMenu(items=menu_items_button, width_mult=5,
                                        caller=self.screen.get_screen("menu").ids.button1)
        self.dropdown2 = MDDropdownMenu(items=menu_items_button2, width_mult=5,
                                        caller=self.screen.get_screen("menu").ids.button2)
        self.dropdown3 = MDDropdownMenu(items=menu_items_button3, width_mult=5,
                                        caller=self.screen.get_screen("menu").ids.button3)
        self.dropdown4 = MDDropdownMenu(items=menu_items_button4, width_mult=5,
                                        caller=self.screen.get_screen("menu").ids.button4)
        self.dropdown5 = MDDropdownMenu(items=menu_items_button5, width_mult=5,
                                        caller=self.screen.get_screen("menu").ids.button5)

    def clear_text(self):
        self.screen.get_screen("menu").ids.t1.text = " "
        self.screen.get_screen("menu").ids.t2.text = " "
        self.screen.get_screen("menu").ids.t3.text = " "

    def menu_callback(self, text_item, n):
        if n == 1:
            self.screen.get_screen("menu").ids.button1.text = text_item
        elif n == 2:
            self.screen.get_screen("menu").ids.button2.text = text_item
        elif n == 3:
            self.screen.get_screen("menu").ids.button3.text = text_item
        elif n == 4:
            self.screen.get_screen("menu").ids.button4.text = text_item
        elif n == 5:
            self.screen.get_screen("menu").ids.button5.text = text_item

    def Testing(self, option):

        from sklearn import tree
        df = pd.read_csv("Training.csv")

        df.replace(
            {'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                           'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8,
                           'Bronchial Asthma': 9, 'Hypertension ': 10,
                           'Migraine': 11, 'Cervical spondylosis': 12,
                           'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                           'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                           'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                           'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                           'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                           'Varicose veins': 30, 'Hypothyroidism': 31,
                           'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                           '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                           'Psoriasis': 39,
                           'Impetigo': 40}}, inplace=True)
        X = df[self.l1]

        y = df[["prognosis"]]
        np.ravel(y)#two dimentionat arry into one
        # print(y)
        tr = pd.read_csv("Testing.csv")
        tr.replace(
            {'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                           'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8,
                           'Bronchial Asthma': 9, 'Hypertension ': 10,
                           'Migraine': 11, 'Cervical spondylosis': 12,
                           'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                           'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                           'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                           'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                           'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                           'Varicose veins': 30, 'Hypothyroidism': 31,
                           'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                           '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                           'Psoriasis': 39,
                           'Impetigo': 40}}, inplace=True)
        X_test = tr[self.l1]
        y_test = tr[["prognosis"]]
        np.ravel(y_test)

        if option == 1:

            clf3 = tree.DecisionTreeClassifier()  # empty model of the decision tree
            clf3 = clf3.fit(X.values, y.values)#training the model

            # calculating accuracy-------------------------------------------------------------------
            from sklearn.metrics import accuracy_score
            y_pred = clf3.predict(X_test.values)#after training the model can be used for predicting using predict function
            print("accuracy score")
            print(accuracy_score(y_test, y_pred))
            print(accuracy_score(y_test, y_pred, normalize=False))
            # -----------------------------------------------------
            symptom1 = self.screen.get_screen("menu").ids.button1.text
            symptom2 = self.screen.get_screen("menu").ids.button2.text
            symptom3 = self.screen.get_screen("menu").ids.button3.text
            symptom4 = self.screen.get_screen("menu").ids.button4.text
            symptom5 = self.screen.get_screen("menu").ids.button5.text
            psymptoms = [symptom1, symptom2, symptom3, symptom4,
                         symptom5]  # to get from button

            for k in range(0, len(self.l1)):
                # print (k,)               #put one if the symptom is present
                for z in psymptoms:
                    if z == self.l1[k]:
                        self.l2[k] = 1

            inputtest = [self.l2] #input matrix to test
            predict = clf3.predict(inputtest) #to predict with gicven input
            predicted = predict[0]

            h = 'no'
            a = 0
            for a in range(0, len(self.disease)):
                if predicted == a:
                    h = 'yes'
                    break

            if h == 'yes':
                self.screen.get_screen("menu").ids.t1.text = self.disease[a]
                #print(self.disease[a])
            else:
                self.screen.get_screen("menu").ids.t1.text = "Not Found"
            toast("Test Completed")
        elif option == 2:

            from sklearn.ensemble import RandomForestClassifier
            clf4 = RandomForestClassifier()
            clf4 = clf4.fit(X.values, np.ravel(y))

            # calculating accuracy-------------------------------------------------------------------
            from sklearn.metrics import accuracy_score
            y_pred = clf4.predict(X_test.values)
            print(accuracy_score(y_test, y_pred))
            print(accuracy_score(y_test, y_pred, normalize=False))
            # -----------------------------------------------------
            symptom1 = self.screen.get_screen("menu").ids.button1.text
            symptom2 = self.screen.get_screen("menu").ids.button2.text
            symptom3 = self.screen.get_screen("menu").ids.button3.text
            symptom4 = self.screen.get_screen("menu").ids.button4.text
            symptom5 = self.screen.get_screen("menu").ids.button5.text
            psymptoms = [symptom1, symptom2, symptom3, symptom4,
                         symptom5]  # to get from button

            for k in range(0, len(self.l1)):
                for z in psymptoms:
                    if z == self.l1[k]:
                        self.l2[k] = 1

            inputtest = [self.l2]
            predict = clf4.predict(inputtest)
            predicted = predict[0]

            h = 'no'
            a = 0
            for a in range(0, len(self.disease)):
                if predicted == a:
                    h = 'yes'
                    break

            if h == 'yes':
                self.screen.get_screen("menu").ids.t2.text = self.disease[a]
                #print(self.disease[a])
            else:
                self.screen.get_screen("menu").ids.t2.text = "Not Found"
            toast("Test Completed")
        elif option == 3:

            from sklearn.naive_bayes import GaussianNB
            gnb = GaussianNB()
            gnb = gnb.fit(X.values, np.ravel(y))

            # calculating accuracy-------------------------------------------------------------------
            from sklearn.metrics import accuracy_score
            y_pred = gnb.predict(X_test.values)
            print(accuracy_score(y_test, y_pred))
            print(accuracy_score(y_test, y_pred, normalize=False))
            # -----------------------------------------------------
            symptom1 = self.screen.get_screen("menu").ids.button1.text
            symptom2 = self.screen.get_screen("menu").ids.button2.text
            symptom3 = self.screen.get_screen("menu").ids.button3.text
            symptom4 = self.screen.get_screen("menu").ids.button4.text
            symptom5 = self.screen.get_screen("menu").ids.button5.text
            psymptoms = [symptom1, symptom2, symptom3, symptom4,
                         symptom5]  # to get from button
            for k in range(0, len(self.l1)):
                for z in psymptoms:
                    if z == self.l1[k]:
                        self.l2[k] = 1

            inputtest = [self.l2]
            predict = gnb.predict(inputtest)
            predicted = predict[0]

            h = 'no'
            a = 0
            for a in range(0, len(self.disease)):
                if predicted == a:
                    h = 'yes'
                    break

            if h == 'yes':
                self.screen.get_screen("menu").ids.t3.text = self.disease[a]
                #print(self.disease[a])
            else:
                self.screen.get_screen("menu").ids.t1.text = "Not found"
            toast("Test Completed")
    def build(self):
        return self.screen


MlDoctor().run()
