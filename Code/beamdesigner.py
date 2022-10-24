from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import math
from tooltips import CreateToolTip
from tkinter import messagebox
import ast
import re
import ctypes

#BEAM DESIGNER TOOL
#CREATED BY GEORGES ELKASSOUF
#02/2021
#-------------------------------------------------------------------------------


CharacterCheck = re.compile('^-?\d*\.?\d*$')

def defocus(event):
   event.widget.master.focus_set()

root = Tk()

#image
canvas = Canvas(root, width = 510, height = 300)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("posmoment.png"))
canvas.create_image(320, 43, anchor=NE, image=img)
img1 = ImageTk.PhotoImage(Image.open("negmoment.png"))
canvas.create_image(515, 43, anchor=NE, image=img1)

#icon
root.wm_iconbitmap('icon.ico')
root.title("Beam Designer")

#geometry
root.geometry ("550x655")
root.resizable(width = False, height = False)
ctypes.windll.shcore.SetProcessDpiAwareness(True)



def imperial():

    mpa1 = Label(root)
    mpa2 = Label(root)
    ksi1 = Label(root)
    ksi2 = Label(root)
    mm1 = Label(root)
    mm2 = Label(root)
    mm3 = Label(root)
    mm4 = Label(root)
    mm5 = Label(root)
    inch1 = Label(root)
    inch2 = Label(root)
    inch3 = Label(root)
    inch4 = Label(root)
    inch5 = Label(root)
    mmsquare1 = Label(root)
    mmsquare2 = Label(root)
    mmsquare3 = Label(root)
    mmsquare4 = Label(root)
    insquare1 = Label(root)
    insquare2 = Label(root)
    insquare3 = Label(root)
    insquare4 = Label(root)



    #Diameter of Bars
    d3 = 0.375
    d4 = 0.5
    d5 = 0.625
    d6 = 0.75
    d7 = 0.875
    d8 = 1
    d9 = 1.128
    d10 = 1.27
    d11 = 1.41
    d14 = 1.693
    d18 = 2.257

    #Area of Bars
    a3 = 0.11
    a4 = 0.2
    a5 = 0.31
    a6 = 0.44
    a7 = 0.6
    a8 = 0.79
    a9 = 1
    a10 = 1.27
    a11 = 1.56
    a14 = 2.25
    a18 = 4


    #ButtonsFunctions

    def calculate():

     e8.focus()

     if e1.get() == "" or e2.get() == "" or e3.get() == "" or e4.get() == "" or e5.get() == "" or e12.get() == "" or e13.get() == "":
        messagebox.showerror("Empty Field", "Some fields are left empty")

     elif CharacterCheck.match(e1.get()) is None or CharacterCheck.match(e2.get()) is None or CharacterCheck.match(e3.get()) is None or CharacterCheck.match(e4.get()) is None or CharacterCheck.match(e5.get()) is None or CharacterCheck.match(e6.get()) is None or CharacterCheck.match(e7.get()) is None or CharacterCheck.match(e12.get()) is None or CharacterCheck.match(e13.get()) is None:
        messagebox.showerror("Unsupported Character", "Unsupported characters detected")

     elif float(e1.get()) <= 0 or float(e2.get()) <= 0 or float(e3.get()) <= 0 or float(e4.get()) <= 0 or float(e5.get()) <= 0 or float(e12.get()) <= 0 or float(e13.get()) <= 0 or float(e6.get()) <= 0:
        messagebox.showerror("Unsupported Value", "Fields cannot be less or equal to zero")

     else:

            #BarDesignation

            #POSITIVE

            if barnumberpos.get() == barnopos[0]:
                Area1 = a3
                diameter1 = d3
            elif barnumberpos.get() == barnopos[1]:
                Area1 = a4
                diameter1 = d4
            elif barnumberpos.get() == barnopos[2]:
                Area1 = a5
                diameter1 = d5
            elif barnumberpos.get() == barnopos[3]:
                Area1 = a6
                diameter1 = d6
            elif barnumberpos.get() == barnopos[4]:
                Area1 = a7
                diameter1 = d7
            elif barnumberpos.get() == barnopos[5]:
                Area1 = a8
                diameter1 = d8
            elif barnumberpos.get() == barnopos[6]:
                Area1 = a9
                diameter1 = d9
            elif barnumberpos.get() == barnopos[7]:
                Area1 = a10
                diameter1 = d10
            elif barnumberpos.get() == barnopos[8]:
                Area1 = a11
                diameter1 = d11
            elif barnumberpos.get() == barnopos[9]:
                Area1 = a14
                diameter1 = d14
            else:
                Area1 = a18
                diameter1 = d18

            Areapos = int(noOfBarspos.get()) * Area1


            #NEGATIVE

            if barnumberneg.get() == barnoneg[0]:
                Area2 = a3
                diameter2 = d3
            elif barnumberneg.get() == barnoneg[1]:
                Area2 = a4
                diameter2 = d4
            elif barnumberneg.get() == barnoneg[2]:
                Area2 = a5
                diameter2 = d5
            elif barnumberneg.get() == barnoneg[3]:
                Area2 = a6
                diameter2 = d6
            elif barnumberneg.get() == barnoneg[4]:
                Area2 = a7
                diameter2 = d7
            elif barnumberneg.get() == barnoneg[5]:
                Area2 = a8
                diameter2 = d8
            elif barnumberneg.get() == barnoneg[6]:
                Area2 = a9
                diameter2 = d9
            elif barnumberneg.get() == barnoneg[7]:
                Area2 = a10
                diameter2 = d10
            elif barnumberneg.get() == barnoneg[8]:
                Area2 = a11
                diameter2 = d11
            elif barnumberneg.get() == barnoneg[9]:
                Area2 = a14
                diameter2 = d14
            else:
                Area2 = a18
                diameter2 = d18

            Areaneg = int(noOfBarsneg.get()) * Area2


            e8.config(state='normal')
            e9.config(state='normal')
            e10.config(state='normal')
            e11.config(state='normal')
            e14.config(state='normal')
            e15.config(state='normal')
            e16.config(state='normal')
            e17.config(state='normal')
            e18.config(state='normal')
            e19.config(state='normal')


            e8.delete(0, END)
            e9.delete(0, END)
            e10.delete(0, END)
            e11.delete(0, END)
            e14.delete(0, END)
            e15.delete(0, END)
            e16.delete(0, END)
            e17.delete(0, END)
            e18.delete(0, END)
            e19.delete(0, END)


            ne1 = float(e1.get())
            ne2 = float(e2.get())
            ne3 = float(e3.get())
            ne4 = float(e4.get())
            ne5 = float(e5.get())
            ne12 = float(e12.get())
            ne13 = float(e13.get())


            if len(e7.get()) == 0:
                ne7 = 0
                e7.insert(0, 0)

            else:

             nne7 = ast.literal_eval (e7.get())

             if isinstance(nne7, int) is True:
                ne7 = abs(int(e7.get()))
                e7.delete(0, END)
                e7.insert(0, (ne7))

             else:
                ne7 = abs(float(e7.get()))
                e7.delete(0, END)
                e7.insert(0, (ne7))


            if len(e6.get()) == 0:
                ne6 = 0
                e6.insert(0, 0)
            else:
                ne6 = float(e6.get())


            #DEPTH d
            depthdpos = ne4 - ne12 - 0.375 - (0.5*diameter1)
            depthdneg = ne4 - ne5 - 0.375 - (0.5*diameter2)


            #MINIMUM WIDTH
            maxspacingpos = max(diameter1, 1)
            maxspacingneg = max(diameter2, 1)

            if diameter1 == d3 or d4 or d5 or d6 or d7 or d8 or d9 or d10 or d11:

                bminpos1 = ne13*2 + (2*0.375) + (diameter1*int(noOfBarspos.get())) + maxspacingpos*(int(noOfBarspos.get()) - 1) + 2*((2*0.375)-(diameter1*0.5))
                bminpos = int(math.ceil(bminpos1 / 0.5)) * 0.5

            else:
                bminpos1 = ne13*2 + (2*0.375) + (diameter1*int(noOfBarspos.get())) + maxspacingpos*(int(noOfBarspos.get()) - 1)
                bminpos = int(math.ceil(bminpos1 / 0.5)) * 0.5

            if diameter2 == d3 or d4 or d5 or d6 or d7 or d8 or d9 or d10 or d11:

                bminneg1 = ne13*2 + (2*0.375) + (diameter2*int(noOfBarsneg.get())) + maxspacingneg*(int(noOfBarsneg.get()) - 1) + 2*((2*0.375)-(diameter2*0.5))
                bminneg = int(math.ceil(bminneg1 / 0.5)) * 0.5

            else:
                bminneg1 = ne13*2 + (2*0.375) + (diameter2*int(noOfBarsneg.get())) + maxspacingneg*(int(noOfBarsneg.get()) - 1)
                bminneg = int(math.ceil(bminneg1 / 0.5)) * 0.5


            if ne1 < 4:
                betta = 0.85

            elif ne1 > 8:
                betta = 0.65

            else:
                betta = 0.85 - 0.05*((ne1*1000) - 4000)/1000


            #POSITIVE REINFORCEMENT
            if ne6 > 0:

                e16.insert(0, round(Areapos, 2))
            else:
                e16.insert(0, "")

            if ne6 == 0:
                e18.insert(0, "")
                e8.config(state='readonly')
                e9.config(state='readonly')
                e15.config(state='readonly')
                e16.config(state='readonly')
                e18.config(state='readonly')

            else:

             Rn = (ne6*12) / (0.9 * ne3 * depthdpos**2)
             if ((2*Rn) / (0.85*ne1)) > 1:

                e16.delete(0, END)

                e9.config(state='readonly')
                e8.config(state='readonly')
                e16.config(state='readonly')
                e15.config(state='readonly')
                e18.config(state='readonly')


             else:
                rho = ((0.85*(ne1/ne2)) * (1 - math.sqrt(1 - (2*Rn) / (0.85*ne1))))

                Asposreq = rho * ne3 * depthdpos
                e18.insert(0, round(Asposreq,2))

                if Areapos < Asposreq:
                    e9.insert(0, "Area of steel provided is less than the required")

                    e9.config(state='readonly')
                    e8.config(state='readonly')
                    e16.config(state='readonly')
                    e15.config(state='readonly')
                    e18.config(state='readonly')

                else:

                    if ne2 <= 80:
                        Area1minpos = ((3*(math.sqrt(ne1*1000))/(ne2*1000))*(ne3 * depthdpos))
                        Area2minpos = ((200*ne3*depthdpos)/(ne2*1000))

                    else:
                        Area1minpos = ((3*(math.sqrt(ne1*1000))/(80*1000))*(ne3 * depthdpos))
                        Area2minpos = ((200*ne3*depthdpos)/(80*1000))

                    if Areapos >= (4/3)*Asposreq or Areapos >= max((Area1minpos),(Area2minpos)):

                     a = ((Areapos*ne2)/(0.85*ne1*ne3))

                     c = (a/betta)

                     Mn = ((ne2*Areapos) * (depthdpos-(a/2)))/12

                     epsilon = ((depthdpos - c) / (c)) * 0.003

                     if epsilon < 0.005:

                      e9.insert(0, "Section not ductile, strain < 0.005")

                     else:
                        if ne3 < bminpos:
                         e9.insert (0, "Unsufficient beam width")
                        else:
                         result = round((0.9 * Mn),2)
                         e8.insert(0, float(result))
                         DOverCPOS = round ((ne6/result),2)
                         e15.insert(0, float(DOverCPOS))

                        if result >= ne6:
                            if ne4 > 36:
                                e9.insert(0, "Section is OK, Skin reinf. needed for h > 36in")
                            else:
                                e9.insert (0, "Section is OK")

                        else:
                                e9.insert (0, "Section is not OK")

                    else:

                     e9.insert (0, "Rho is less than the minimum")

                     e8.config(state='readonly')
                     e9.config(state='readonly')
                     e15.config(state='readonly')
                     e16.config(state='readonly')
                     e18.config(state='readonly')


            #NEGATIVE REINFORCEMENT

            if ne7 > 0:

                e17.insert(0, round(Areaneg, 2))
            else:
                e17.insert(0, "")

            if ne7 == 0:
                e19.insert(0, "")
                e10.config(state='readonly')
                e11.config(state='readonly')
                e14.config(state='readonly')
                e17.config(state='readonly')
                e19.config(state='readonly')

            else:

                Rn = (ne7*12) / (0.9 * ne3 * depthdneg**2)
                if ((2*Rn) / (0.85*ne1)) > 1:

                 e17.delete(0, END)

                 e10.config(state='readonly')
                 e11.config(state='readonly')
                 e19.config(state='readonly')
                 e14.config(state='readonly')
                 e17.config(state='readonly')

                else:

                 rho = ((0.85*(ne1/ne2)) * (1 - math.sqrt(1 - (2*Rn) / (0.85*ne1))))
                 Asnegreq = rho * ne3 * depthdneg
                 e19.insert(0, round(Asnegreq,2))

                 if Areaneg < Asnegreq:
                    e10.insert(0, "Area of steel provided is less than the required")

                    e10.config(state='readonly')
                    e11.config(state='readonly')
                    e19.config(state='readonly')
                    e14.config(state='readonly')
                    e17.config(state='readonly')

                 else:

                    if ne2 <= 80:
                     Area1minneg = ((3*(math.sqrt(ne1*1000))/(ne2*1000))*(ne3 * depthdneg))
                     Area2minneg = ((200*ne3*depthdneg)/(ne2*1000))

                    else:
                     Area1minneg = ((3*(math.sqrt(ne1*1000))/(80*1000))*(ne3 * depthdneg))
                     Area2minneg = ((200*ne3*depthdneg)/(80*1000))

                    if Areaneg >= (4/3)*Asnegreq or Areaneg >= max((Area1minneg),(Area2minneg)):

                     a = ((Areaneg*ne2)/(0.85*ne1*ne3))

                     c = (a/betta)

                     Mn = ((ne2*Areaneg) * (depthdneg-(a/2)))/12

                     epsilon = ((depthdneg - c) / (c)) * 0.003

                     if epsilon < 0.005:
                      e10.insert(0, "Section not ductile, strain < 0.005")

                     else:
                        if ne3 < bminneg:
                         e10.insert (0, "Unsufficient beam width")
                        else:
                         result = round((0.9 * Mn),2)
                         e11.insert(0, float(result))
                         DOverCNEG = round ((ne7/result),2)
                         e14.insert(0, float(DOverCNEG))

                        if result >= ne7:
                            if ne4 > 36:
                                e10.insert(0, "Section is OK, Skin reinf. needed for h > 36in")
                            else:
                                e10.insert (0, "Section is OK")
                        else:
                                e10.insert (0, "Section is not OK")

                    else:

                     e10.insert (0, "Rho is less than the minimum")

                     e10.config(state='readonly')
                     e11.config(state='readonly')
                     e14.config(state='readonly')
                     e17.config(state='readonly')
                     e19.config(state='readonly')



    def clear():

        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e12.delete(0,END)
        e13.delete(0,END)
        e8.config(state='normal')
        e9.config(state='normal')
        e10.config(state='normal')
        e11.config(state='normal')
        e14.config(state='normal')
        e15.config(state='normal')
        e16.config(state='normal')
        e17.config(state='normal')
        e18.config(state='normal')
        e19.config(state='normal')
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        e11.delete(0,END)
        e14.delete(0,END)
        e15.delete(0,END)
        e16.delete(0,END)
        e17.delete(0,END)
        e18.delete(0,END)
        e19.delete(0,END)
        e8.config(state='readonly')
        e9.config(state='readonly')
        e10.config(state='readonly')
        e11.config(state='readonly')
        e14.config(state='readonly')
        e15.config(state='readonly')
        e16.config(state='readonly')
        e17.config(state='readonly')
        e18.config(state='readonly')
        e19.config(state='readonly')
        barnumberpos.bind("<<ComboboxSelected>>", barnumberpos.current(0))
        noOfBarspos.bind("<<ComboboxSelected>>", noOfBarspos.current(0))
        barnumberneg.bind("<<ComboboxSelected>>", barnumberneg.current(0))
        noOfBarsneg.bind("<<ComboboxSelected>>", noOfBarsneg.current(0))
        e8.focus()


    #FunctionsForCombos

    barnopos = [
    "#3",
    "#4",
    "#5",
    "#6",
    "#7",
    "#8",
    "#9",
    "#10",
    "#11",
    "#14",
    "#18"
    ]

    barcountpos = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    ]


    barnoneg = [
    "#3",
    "#4",
    "#5",
    "#6",
    "#7",
    "#8",
    "#9",
    "#10",
    "#11",
    "#14",
    "#18"
    ]

    barcountneg = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    ]


    #Combos
    #Combo for Positive Reinforcement

    barnumberpos = ttk.Combobox(root, value = barnopos, width =5, justify = 'center')
    barnumberpos.current(0)
    barnumberpos.place(x=430, y = 320)
    barnumberpos.bind("<<ComboboxSelected>>", lambda e: e8.focus())


    noOfBarspos = ttk.Combobox(root, value = barcountpos, width =5, justify = 'center')
    noOfBarspos.current(0)
    noOfBarspos.place(x=370, y = 320)
    noOfBarspos.bind("<<ComboboxSelected>>", lambda e: e8.focus())


    #Combo for Negative Reinforcement

    barnumberneg = ttk.Combobox(root, value = barnoneg, width =5, justify = 'center')
    barnumberneg.current(0)
    barnumberneg.place(x=430, y = 350)
    barnumberneg.bind("<<ComboboxSelected>>", lambda e: e8.focus())


    noOfBarsneg = ttk.Combobox(root, value = barcountneg, width =5, justify = 'center')
    noOfBarsneg.current(0)
    noOfBarsneg.place(x=370, y = 350)
    noOfBarsneg.bind("<<ComboboxSelected>>", lambda e: e8.focus())



    #labels

    compstrength = Label(root, text= "f'c", font = 'Calibri 11', fg = 'black')
    compstrength.place(x=5, y = 70)

    yieldstrength = Label(root, text= "fy", font = 'Calibri 11', fg = 'black')
    yieldstrength.place(x=5, y =100)

    beamwidth = Label(root, text= "b", font = 'Calibri 11', fg = 'black')
    beamwidth.place(x=5, y =130)

    beamdepth = Label(root, text= "h", font = 'Calibri 11', fg = 'black')
    beamdepth.place(x=5, y =160)

    cover = Label(root, text= " Covers", font = 'Calibri 11 bold', fg = 'black')
    cover.place(x=75, y =260)

    topcover = Label(root, text= "Clear Cover at Top", font = 'Calibri 10', fg = 'black')
    topcover.place(x=3, y =290)

    bottomcover = Label(root, text= "Clear Cover at Bottom", font = 'Calibri 10', fg = 'black')
    bottomcover.place(x=3, y =320)

    sidecover = Label(root, text= "Clear Cover at Sides", font = 'Calibri 10', fg = 'black')
    sidecover.place(x=3, y =350)

    Mupos = Label(root, text= "Mu\u207A", font = 'Calibri 11', fg = 'black')
    Mupos.place(x=1, y =190)

    Muneg = Label(root, text= "Mu\u207B", font = 'Calibri 11', fg = 'black')
    Muneg.place(x=1, y =220)

    posreinf = Label(root, text= "Bottom Reinforcement", font = 'Calibri 10', fg = 'black')
    posreinf.place(x=230, y =320)

    negreinf = Label(root, text= "Top Reinforcement", font = 'Calibri 10', fg = 'black')
    negreinf.place(x=230, y =350)

    posreinfres = Label(root, text= "Positive Moment", font = 'Calibri 11 bold', fg = 'black')
    posreinfres.place(x=50, y =380)

    negreinfres = Label(root, text= "Negative Moment", font = 'Calibri 11 bold', fg = 'black')
    negreinfres.place(x=320, y =380)

    ReinfTitle = Label(root, text= "Reinforcement", font = 'Calibri 11 bold', fg = 'black')
    ReinfTitle.place(x=330, y =287)

    MainTitle = Label(root, text = "RC Beam Design", font = 'Calibri 14 bold', fg = 'black')
    MainTitle.place(x=275, y = 14, anchor = CENTER)

    Outcomepos = Label(root, text= "Section Capacity", font = 'Calibri 10', fg = 'black')
    Outcomepos.place(x=67, y =480, anchor = CENTER)

    Outcomeneg = Label(root, text= "Section Capacity", font = 'Calibri 10', fg = 'black')
    Outcomeneg.place(x=340, y =480, anchor = CENTER)

    DCPOS = Label(root, text= "D/C Ratio", font = 'Calibri 10', fg = 'black')
    DCPOS.place(x=67, y =510, anchor = CENTER)

    DCNEG = Label(root, text= "D/C Ratio", font = 'Calibri 10', fg = 'black')
    DCNEG.place(x=340, y =510, anchor = CENTER)

    AsProvPOS = Label(root, text= "As Provided", font = 'Calibri 10', fg = 'black')
    AsProvPOS.place(x=67, y =450, anchor = CENTER)

    AsProvNEG = Label(root, text= "As Provided", font = 'Calibri 10', fg = 'black')
    AsProvNEG.place(x=340, y =450, anchor = CENTER)

    AsReqPOS = Label(root, text= "As Required", font = 'Calibri 10', fg = 'black')
    AsReqPOS.place(x=67, y =420, anchor = CENTER)

    AsReqNEG = Label(root, text= "As Required", font = 'Calibri 10', fg = 'black')
    AsReqNEG.place(x=340, y =420, anchor = CENTER)

    created = Label(root, text= "Created by Georges Elkassouf", font = 'Calibri 8', fg = 'black')
    created.place(x=0, y =655, anchor = SW)

    date = Label(root, text= "02/2021", font = 'Calibri 8', fg = 'black')
    date.place(x=550, y =655, anchor = SE)

    code = Label(root, text = "ACI 318-19", font = 'Calibri 9', fg = 'black')
    code.place(x=545, y = 20, anchor = NE)

    unitsystem = Label(root, text = "Unit System", font = 'Calibri 9 bold', fg = 'black')
    unitsystem.place(x=5, y = 33, anchor = SW)

    designcode = Label(root, text = "Design Code", font = 'Calibri 9 bold', fg = 'black')
    designcode.place(x=480, y = 20, anchor = SW)


    ############################################################################

    ############################################################################

    #units

    ksi1d = Label(root, text= "Ksi", font = 'Calibri 11', fg = 'black')
    ksi1d.place(x=95, y =70)

    ksi2d = Label(root, text= "Ksi", font = 'Calibri 11', fg = 'black')
    ksi2d.place(x=95, y =100)

    inch1d = Label(root, text= "in", font = 'Calibri 11', fg = 'black')
    inch1d.place(x=95, y =130)

    inch2d = Label(root, text= "in", font = 'Calibri 11', fg = 'black')
    inch2d.place(x=95, y =160)

    inch3d = Label(root, text= "in", font = 'Calibri 10', fg = 'black')
    inch3d.place(x=182, y =288)

    inch4d = Label(root, text= "in", font = 'Calibri 10', fg = 'black')
    inch4d.place(x=182, y =318)

    inch5d = Label(root, text= "in", font = 'Calibri 10', fg = 'black')
    inch5d.place(x=182, y =348)

    kipft1 = Label(root, text= "Kip.ft", font = 'Calibri 11', fg = 'black')
    kipft1.place(x=95, y =189)

    kipft2 = Label(root, text= "Kip.ft", font = 'Calibri 11', fg = 'black')
    kipft2.place(x=95, y =217)

    kipft3 = Label(root, text= "Kip.ft", font = 'Calibri 10', fg = 'black')
    kipft3.place(x=190, y =480, anchor = CENTER)

    kipft4 = Label(root, text= "Kip.ft", font = 'Calibri 10', fg = 'black')
    kipft4.place(x=465, y =480, anchor = CENTER)

    insquare1d = Label(root, text= "in\u00B2", font = 'Calibri 10', fg = 'black')
    insquare1d.place(x=184, y =450, anchor = CENTER)

    insquare2d = Label(root, text= "in\u00B2", font = 'Calibri 10', fg = 'black')
    insquare2d.place(x=459, y =450, anchor = CENTER)

    insquare3d = Label(root, text= "in\u00B2", font = 'Calibri 10', fg = 'black')
    insquare3d.place(x=459, y =420, anchor = CENTER)

    insquare4d = Label(root, text= "in\u00B2", font = 'Calibri 10', fg = 'black')
    insquare4d.place(x=184, y =420, anchor = CENTER)


    #Buttons

    CalculateButton = Button(root, text= "Calculate", font = 'Calibri 14 bold', fg = 'black', command = calculate, relief = SOLID)
    CalculateButton.place(x=275, y =580, anchor = CENTER)

    ClearButton = Button(root, text= "Clear", font = 'Calibri 12 bold', fg = 'black', height = 1, command = clear, relief = GROOVE)
    ClearButton.place(x=275, y =620, anchor = CENTER)

    #Entries

    #f'c
    e1 = Entry(root, width =8, justify = 'center')
    e1.place(x=43, y =73)

    #fy
    e2 = Entry(root,width =8, justify = 'center')
    e2.place(x=43, y =103)

    #width
    e3 = Entry(root,width =8, justify = 'center')
    e3.place(x=43, y =133)

    #depth
    e4 = Entry(root,width =8, justify = 'center')
    e4.place(x=43, y =163)

    #Mu+
    e6 = Entry(root, width =8, justify = 'center')
    e6.place(x=43, y =190)

    #Mu-
    e7 = Entry(root, width =8, justify = 'center')
    e7.place(x=43, y =220)

    #topcover
    e5 = Entry(root,width =8, justify = 'center')
    e5.place(x=130, y =290)

    #bottomcover
    e12 = Entry(root,width =8, justify = 'center')
    e12.place(x=130, y =320)

    #sidecover
    e13 = Entry(root,width =8, justify = 'center')
    e13.place(x=130, y =350)

    #Capacity for Positive Moment
    e8 = Entry(root,width =8, justify = 'center')
    e8.place(x=145, y =480, anchor = CENTER)

    #Result for Positive Moment
    e9 = Entry(root, width =38, font = 'Calibri 8', fg = 'red', justify = 'center')
    e9.place(x=135, y =540, anchor = CENTER)

    #Result for Negative Moment
    e10 = Entry(root, width =38, font = 'Calibri 8', fg = 'red', justify = 'center')
    e10.place(x=410, y =540, anchor = CENTER)

    #Capacity for Negative Moment
    e11 = Entry(root,width =8, justify = 'center')
    e11.place(x=420, y =480, anchor = CENTER)

    #Negative D/C Ratio
    e14 = Entry(root,width =8, justify = 'center')
    e14.place(x=420, y =510, anchor = CENTER)

    #Positive D/C Ratio
    e15 = Entry(root,width =8, justify = 'center')
    e15.place(x=145, y =510, anchor = CENTER)

    #Positive Area of Steel Provided
    e16 = Entry(root,width =8, justify = 'center')
    e16.place(x=145, y =450, anchor = CENTER)

    #Negative Area of Steel Provided
    e17 = Entry(root,width =8, justify = 'center')
    e17.place(x=420, y =450, anchor = CENTER)

    #Positive Area of Steel Required
    e18 = Entry(root,width =8, justify = 'center')
    e18.place(x=145, y =420, anchor = CENTER)

    #Negative Area of Steel Required
    e19 = Entry(root,width =8, justify = 'center')
    e19.place(x=420, y =420, anchor = CENTER)


    e8.config(state='readonly')
    e9.config(state='readonly')
    e10.config(state='readonly')
    e11.config(state='readonly')
    e14.config(state='readonly')
    e15.config(state='readonly')
    e16.config(state='readonly')
    e17.config(state='readonly')
    e18.config(state='readonly')
    e19.config(state='readonly')

    #ToolTips

    CreateToolTip(e1, 'Compressive Strength of Concrete')
    CreateToolTip(e2, 'Tensile Strength of Steel')
    CreateToolTip(e3, 'Beam Width')
    CreateToolTip(e4, 'Beam Depth')
    CreateToolTip(e5, 'Top Clear Cover')
    CreateToolTip(e6, 'Factored Positive Moment')
    CreateToolTip(e7, 'Factored Negative Moment in Absolute Value')
    CreateToolTip(e8, 'Section Capacity for Positive Moment')
    CreateToolTip(e9, 'Calculation Results for Positive Moment')
    CreateToolTip(e10, 'Calculation Results for Negative Moment')
    CreateToolTip(e11, 'Section Capacity for Negative Moment')
    CreateToolTip(e12, 'Bottom Clear Cover')
    CreateToolTip(e13, 'Side Clear Cover')
    CreateToolTip(e14, 'Demand over Capacity Ratio for Negative Moment')
    CreateToolTip(e15, 'Demand over Capacity Ratio for Positive Moment')
    CreateToolTip(e16, 'Provided Area of Steel for Positive Moment')
    CreateToolTip(e17, 'Provided Area of Steel for Negative Moment')
    CreateToolTip(e18, 'Required Area of Steel for Positive Moment')
    CreateToolTip(e19, 'Required Area of Steel for Negative Moment')


    def design(event):

        global ksi1d
        global ksi2d
        global mpa1
        global mpa2
        global inch1d
        global inch2d
        global inch3d
        global inch4d
        global inch5d
        global mm1
        global mm2
        global mm3
        global mm4
        global mm5
        global mmsquare1
        global mmsquare2
        global mmsquare3
        global mmsquare4
        global insquare1d
        global insquare2d
        global insquare3d
        global insquare4d

        ksi1d.destroy()
        ksi2d.destroy()
        mpa1.destroy()
        mpa2.destroy()
        inch1d.destroy()
        inch2d.destroy()
        inch3d.destroy()
        inch4d.destroy()
        inch5d.destroy()
        mm1.destroy()
        mm2.destroy()
        mm3.destroy()
        mm4.destroy()
        mm5.destroy()
        mmsquare1.destroy()
        mmsquare2.destroy()
        mmsquare3.destroy()
        mmsquare4.destroy()
        insquare1d.destroy()
        insquare2d.destroy()
        insquare3d.destroy()
        insquare4d.destroy()


    if unitbox.get() == units[0]:

        imperial()

    else:

        ksi1d.destroy()
        ksi2d.destroy()
        inch1d.destroy()
        inch2d.destroy()
        inch3d.destroy()
        inch4d.destroy()
        inch5d.destroy()
        insquare1d.destroy()
        insquare2d.destroy()
        insquare3d.destroy()

        #Diameter of Bars
        d10 = 9.5
        d13 = 12.7
        d16 = 15.9
        d19 = 19.1
        d22 = 22.2
        d25 = 25.4
        d29 = 28.7
        d32 = 32.3
        d36 = 35.8
        d43 = 43
        d57 = 57.3

        #Area of Bars
        a10 = 71
        a13 = 129
        a16 = 199
        a19 = 284
        a22 = 387
        a25 = 510
        a29 = 645
        a32 = 819
        a36 = 1006
        a43 = 1452
        a57 = 2581

        #ButtonsFunctions

        def calculate():

            e8.focus()

            if e1.get() == "" or e2.get() == "" or e3.get() == "" or e4.get() == "" or e5.get() == "" or e12.get() == "" or e13.get() == "":
                messagebox.showerror("Empty Field", "Some fields are left empty")

            elif CharacterCheck.match(e1.get()) is None or CharacterCheck.match(e2.get()) is None or CharacterCheck.match(e3.get()) is None or CharacterCheck.match(e4.get()) is None or CharacterCheck.match(e5.get()) is None or CharacterCheck.match(e6.get()) is None or CharacterCheck.match(e7.get()) is None or CharacterCheck.match(e12.get()) is None or CharacterCheck.match(e13.get()) is None:
                messagebox.showerror("Unsupported Character", "Unsupported characters detected")

            elif float(e1.get()) <= 0 or float(e2.get()) <= 0 or float(e3.get()) <= 0 or float(e4.get()) <= 0 or float(e5.get()) <= 0 or float(e12.get()) <= 0 or float(e13.get()) <= 0 or float(e6.get()) <= 0:
                messagebox.showerror("Unsupported Value", "Fields cannot be less or equal to zero")

            else:

                #BarDesignation

                #POSITIVE

                if barnumberpos.get() == barnopos[0]:
                    Area1 = a10
                    diameter1 = d10
                elif barnumberpos.get() == barnopos[1]:
                    Area1 = a13
                    diameter1 = d13
                elif barnumberpos.get() == barnopos[2]:
                    Area1 = a16
                    diameter1 = d16
                elif barnumberpos.get() == barnopos[3]:
                    Area1 = a19
                    diameter1 = d19
                elif barnumberpos.get() == barnopos[4]:
                    Area1 = a22
                    diameter1 = d22
                elif barnumberpos.get() == barnopos[5]:
                    Area1 = a25
                    diameter1 = d25
                elif barnumberpos.get() == barnopos[6]:
                    Area1 = a29
                    diameter1 = d29
                elif barnumberpos.get() == barnopos[7]:
                    Area1 = a32
                    diameter1 = d32
                elif barnumberpos.get() == barnopos[8]:
                    Area1 = a36
                    diameter1 = d36
                elif barnumberpos.get() == barnopos[9]:
                    Area1 = a43
                    diameter1 = d43
                else:
                    Area1 = a57
                    diameter1 = d57

                Areapos = int(noOfBarspos.get()) * Area1


                #NEGATIVE

                if barnumberneg.get() == barnoneg[0]:
                    Area2 = a10
                    diameter2 = d10
                elif barnumberneg.get() == barnoneg[1]:
                    Area2 = a13
                    diameter2 = d13
                elif barnumberneg.get() == barnoneg[2]:
                    Area2 = a16
                    diameter2 = d16
                elif barnumberneg.get() == barnoneg[3]:
                    Area2 = a19
                    diameter2 = d19
                elif barnumberneg.get() == barnoneg[4]:
                    Area2 = a22
                    diameter2 = d22
                elif barnumberneg.get() == barnoneg[5]:
                    Area2 = a25
                    diameter2 = d25
                elif barnumberneg.get() == barnoneg[6]:
                    Area2 = a29
                    diameter2 = d29
                elif barnumberneg.get() == barnoneg[7]:
                    Area2 = a32
                    diameter2 = d32
                elif barnumberneg.get() == barnoneg[8]:
                    Area2 = a36
                    diameter2 = d36
                elif barnumberneg.get() == barnoneg[9]:
                    Area2 = a43
                    diameter2 = d43
                else:
                    Area2 = a57
                    diameter2 = d57

                Areaneg = int(noOfBarsneg.get()) * Area2


                e8.config(state='normal')
                e9.config(state='normal')
                e10.config(state='normal')
                e11.config(state='normal')
                e14.config(state='normal')
                e15.config(state='normal')
                e16.config(state='normal')
                e17.config(state='normal')
                e18.config(state='normal')
                e19.config(state='normal')



                e8.delete(0, END)
                e9.delete(0, END)
                e10.delete(0, END)
                e11.delete(0, END)
                e14.delete(0, END)
                e15.delete(0, END)
                e16.delete(0, END)
                e17.delete(0, END)
                e18.delete(0, END)
                e19.delete(0, END)


                ne1 = float(e1.get())
                ne2 = float(e2.get())
                ne3 = float(e3.get())
                ne4 = float(e4.get())
                ne5 = float(e5.get())
                ne12 = float(e12.get())
                ne13 = float(e13.get())

                if len(e7.get()) == 0:
                    ne7 = 0
                    e7.insert(0, 0)

                else:

                    nne7 = ast.literal_eval (e7.get())

                    if isinstance(nne7, int) is True:
                     ne7 = abs(int(e7.get()))
                     e7.delete(0, END)
                     e7.insert(0, (ne7))

                    else:
                     ne7 = abs(float(e7.get()))
                     e7.delete(0, END)
                     e7.insert(0, (ne7))


                if len(e6.get()) == 0:
                    ne6 = 0
                    e6.insert(0, 0)
                else:
                    ne6 = float(e6.get())


                #DEPTH d
                depthdpos = ne4 - ne12 - 9.5 - (0.5*diameter1)
                depthdneg = ne4 - ne5 - 9.5 - (0.5*diameter2)


                #MINIMUM WIDTH
                maxspacingpos = max(diameter1, 25)
                maxspacingneg = max(diameter2, 25)

                if diameter1 == d10 or d13 or d16 or d19 or d22 or d25 or d29 or d32 or d36:

                   bminpos1 = ne13*2 + (2*9.5) + (diameter1*int(noOfBarspos.get())) + maxspacingpos*(int(noOfBarspos.get()) - 1) + 2*((2*9.5)-(diameter1*0.5))
                   bminpos = int(math.ceil(bminpos1 / 10.0)) * 10

                else:

                   bminpos1 = ne13*2 + (2*9.5) + (diameter1*int(noOfBarspos.get())) + maxspacingpos*(int(noOfBarspos.get()) - 1)
                   bminpos = int(math.ceil(bminpos1 / 10.0)) * 10

                if diameter2 == d10 or d13 or d16 or d19 or d22 or d25 or d29 or d32 or d36:

                   bminneg1 = ne13*2 + (2*9.5) + (diameter2*int(noOfBarsneg.get())) + maxspacingneg*(int(noOfBarsneg.get()) - 1) + 2*((2*9.5)-(diameter2*0.5))
                   bminneg = int(math.ceil(bminneg1 / 10.0)) * 10

                else:

                   bminneg1 = ne13*2 + (2*9.5) + (diameter2*int(noOfBarsneg.get())) + maxspacingneg*(int(noOfBarsneg.get()) - 1)
                   bminneg = int(math.ceil(bminneg1 / 10.0)) * 10


                if ne1 < 28:
                 betta = 0.85

                elif ne1 > 55:
                 betta = 0.65

                else:
                 betta = 0.85 - 0.05*((ne1) - 28)/7


                #POSITIVE REINFORCEMENT

                if ne6 > 0:
                   e16.insert(0, round(Areapos, 2))
                else:
                   e16.insert(0, "")

                if ne6 == 0:
                   e18.insert(0, "")
                   e8.config(state='readonly')
                   e9.config(state='readonly')
                   e15.config(state='readonly')
                   e16.config(state='readonly')
                   e18.config(state='readonly')

                else:

                 Rn = (ne6*1000000) / (0.9 * ne3 * depthdpos**2)
                 if ((2*Rn) / (0.85*ne1)) > 1:

                   e16.delete(0, END)

                   e9.config(state='readonly')
                   e8.config(state='readonly')
                   e16.config(state='readonly')
                   e15.config(state='readonly')
                   e18.config(state='readonly')

                 else:

                     rho = ((0.85*(ne1/ne2)) * (1 - math.sqrt(1 - (2*Rn) / (0.85*ne1))))
                     Asposreq = rho * ne3 * depthdpos
                     e18.insert(0, round(Asposreq,2))

                     if Areapos < Asposreq:
                      e9.insert(0, "Area of steel provided is less than the required")

                      e9.config(state='readonly')
                      e8.config(state='readonly')
                      e16.config(state='readonly')
                      e15.config(state='readonly')
                      e18.config(state='readonly')

                     else:

                      if ne2 <= 550:
                        Area1minpos = ((0.25*(math.sqrt(ne1))/(ne2))*(ne3 * depthdpos))
                        Area2minpos = ((1.4*ne3*depthdpos)/(ne2))

                      else:
                        Area1minpos = ((0.25*(math.sqrt(ne1))/(550))*(ne3 * depthdpos))
                        Area2minpos = ((1.4*ne3*depthdpos)/(550))

                      if Areapos >= (4/3)*Asposreq or Areapos >= max((Area1minpos),(Area2minpos)):

                       a = ((Areapos*ne2)/(0.85*ne1*ne3))

                       c = (a/betta)

                       Mn = ((ne2*Areapos) * (depthdpos-(a/2)))/1000000

                       epsilon = ((depthdpos - c) / (c)) * 0.003

                       if epsilon < 0.005:

                         e9.insert(0, "Section not ductile, strain < 0.005")

                       else:
                         if ne3 < bminpos:
                             e9.insert (0, "Unsufficient beam width")
                         else:
                             result = round((0.9 * Mn),2)
                             e8.insert(0, float(result))
                             DOverCPOS = round ((ne6/result),2)
                             e15.insert(0, float(DOverCPOS))

                             if result >= ne6:
                              if ne4 > 900:
                                  e9.insert(0, "Section is OK, Skin reinf. needed for h > 900mm")
                              else:
                                  e9.insert (0, "Section is OK")

                             else:
                                  e9.insert (0, "Section is not OK")

                      else:

                         e9.insert (0, "Rho is less than the minimum")

                      e8.config(state='readonly')
                      e9.config(state='readonly')
                      e15.config(state='readonly')
                      e16.config(state='readonly')
                      e18.config(state='readonly')



                #NEGATIVE REINFORCEMENT

                if ne7 > 0:
                   e17.insert(0, round(Areaneg, 2))
                else:
                   e17.insert(0, "")

                if ne7 == 0:
                   e19.insert(0, "")
                   e10.config(state='readonly')
                   e11.config(state='readonly')
                   e14.config(state='readonly')
                   e17.config(state='readonly')
                   e19.config(state='readonly')

                else:

                 Rn = (ne7*1000000) / (0.9 * ne3 * depthdneg**2)
                 if ((2*Rn) / (0.85*ne1)) > 1:

                   e17.delete(0, END)

                   e10.config(state='readonly')
                   e11.config(state='readonly')
                   e14.config(state='readonly')
                   e17.config(state='readonly')
                   e19.config(state='readonly')

                 else:

                     rho = ((0.85*(ne1/ne2)) * (1 - math.sqrt(1 - (2*Rn) / (0.85*ne1))))
                     Asnegreq = rho * ne3 * depthdneg
                     e19.insert(0, round(Asnegreq,2))

                     if Areaneg < Asnegreq:
                      e10.insert(0, "Area of steel provided is less than the required")

                      e10.config(state='readonly')
                      e11.config(state='readonly')
                      e19.config(state='readonly')
                      e14.config(state='readonly')
                      e17.config(state='readonly')

                     else:

                      if ne2 <= 550:
                        Area1minneg = ((0.25*(math.sqrt(ne1))/(ne2))*(ne3 * depthdneg))
                        Area2minneg = ((1.4*ne3*depthdneg)/(ne2))

                      else:
                        Area1minneg = ((0.25*(math.sqrt(ne1))/(550))*(ne3 * depthdneg))
                        Area2minneg = ((1.4*ne3*depthdneg)/(550))

                      if Areaneg >= (4/3)*Asnegreq or Areaneg >= max((Area1minneg),(Area2minneg)):

                       a = ((Areaneg*ne2)/(0.85*ne1*ne3))

                       c = (a/betta)

                       Mn = ((ne2*Areaneg) * (depthdneg-(a/2)))/1000000

                       epsilon = ((depthdneg - c) / (c)) * 0.003

                       if epsilon < 0.005:
                         e10.insert(0, "Section not ductile, strain < 0.005")

                       else:
                         if ne3 < bminneg:
                             e10.insert (0, "Unsufficient beam width")
                         else:
                             result = round((0.9 * Mn),2)
                             e11.insert(0, float(result))
                             DOverCNEG = round ((ne7/result),2)
                             e14.insert(0, float(DOverCNEG))

                             if result >= ne7:
                                if ne4 > 900:
                                    e10.insert(0, "Section is OK, Skin reinf. needed for h > 900mm")
                                else:
                                    e10.insert (0, "Section is OK")
                             else:
                                    e10.insert (0, "Section is not OK")

                      else:

                         e10.insert (0, "Rho is less than the minimum")

                      e10.config(state='readonly')
                      e11.config(state='readonly')
                      e14.config(state='readonly')
                      e17.config(state='readonly')
                      e19.config(state='readonly')



        def clear():

             e1.delete(0,END)
             e2.delete(0,END)
             e3.delete(0,END)
             e4.delete(0,END)
             e5.delete(0,END)
             e6.delete(0,END)
             e7.delete(0,END)
             e12.delete(0,END)
             e13.delete(0,END)
             e8.config(state='normal')
             e9.config(state='normal')
             e10.config(state='normal')
             e11.config(state='normal')
             e14.config(state='normal')
             e15.config(state='normal')
             e16.config(state='normal')
             e17.config(state='normal')
             e18.config(state='normal')
             e19.config(state='normal')
             e8.delete(0,END)
             e9.delete(0,END)
             e10.delete(0,END)
             e11.delete(0,END)
             e14.delete(0,END)
             e15.delete(0,END)
             e16.delete(0,END)
             e17.delete(0,END)
             e18.delete(0,END)
             e19.delete(0,END)
             e8.config(state='readonly')
             e9.config(state='readonly')
             e10.config(state='readonly')
             e11.config(state='readonly')
             e14.config(state='readonly')
             e15.config(state='readonly')
             e16.config(state='readonly')
             e17.config(state='readonly')
             e18.config(state='readonly')
             e19.config(state='readonly')
             barnumberpos.bind("<<ComboboxSelected>>", barnumberpos.current(0))
             noOfBarspos.bind("<<ComboboxSelected>>", noOfBarspos.current(0))
             barnumberneg.bind("<<ComboboxSelected>>", barnumberneg.current(0))
             noOfBarsneg.bind("<<ComboboxSelected>>", noOfBarsneg.current(0))
             e8.focus()


        #FunctionsForCombos

        barnopos = [
        "#10",
        "#13",
        "#16",
        "#19",
        "#22",
        "#25",
        "#29",
        "#32",
        "#36",
        "#43",
        "#57"
        ]

        barcountpos = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        ]


        barnoneg = [
        "#10",
        "#13",
        "#16",
        "#19",
        "#22",
        "#25",
        "#29",
        "#32",
        "#36",
        "#43",
        "#57"
        ]

        barcountneg = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        ]


        #Combos

        #Combo for Positive Reinforcement

        barnumberpos = ttk.Combobox(root, value = barnopos, width =5, justify = 'center')
        barnumberpos.current(0)
        barnumberpos.place(x=430, y = 320)
        barnumberpos.bind("<<ComboboxSelected>>", lambda e: e8.focus())


        noOfBarspos = ttk.Combobox(root, value = barcountpos, width =5, justify = 'center')
        noOfBarspos.current(0)
        noOfBarspos.place(x=370, y = 320)
        noOfBarspos.bind("<<ComboboxSelected>>", lambda e: e8.focus())


        #Combo for Negative Reinforcement

        barnumberneg = ttk.Combobox(root, value = barnoneg, width =5, justify = 'center')
        barnumberneg.current(0)
        barnumberneg.place(x=430, y = 350)
        barnumberneg.bind("<<ComboboxSelected>>", lambda e: e8.focus())


        noOfBarsneg = ttk.Combobox(root, value = barcountneg, width =5, justify = 'center')
        noOfBarsneg.current(0)
        noOfBarsneg.place(x=370, y = 350)
        noOfBarsneg.bind("<<ComboboxSelected>>", lambda e: e8.focus())

        ############################################################################

        ############################################################################

        #units

        mpa1 = Label(root, text= "MPa", font = 'Calibri 11', fg = 'black')
        mpa1.place(x=95, y =70)

        mpa2 = Label(root, text= "MPa", font = 'Calibri 11', fg = 'black')
        mpa2.place(x=95, y =100)

        mm1 = Label(root, text= "mm", font = 'Calibri 11', fg = 'black')
        mm1.place(x=95, y =130)

        mm2 = Label(root, text= "mm", font = 'Calibri 11', fg = 'black')
        mm2.place(x=95, y =160)

        mm3 = Label(root, text= "mm", font = 'Calibri 10', fg = 'black')
        mm3.place(x=182, y =288)

        mm4 = Label(root, text= "mm", font = 'Calibri 10', fg = 'black')
        mm4.place(x=182, y =318)

        mm5 = Label(root, text= "mm", font = 'Calibri 10', fg = 'black')
        mm5.place(x=182, y =348)

        kNm1 = Label(root, text= "KN.m", font = 'Calibri 11', fg = 'black')
        kNm1.place(x=95, y =189)

        kNm2 = Label(root, text= "KN.m", font = 'Calibri 11', fg = 'black')
        kNm2.place(x=95, y =217)

        kNm3 = Label(root, text= "KN.m", font = 'Calibri 10', fg = 'black')
        kNm3.place(x=190, y =480, anchor = CENTER)

        kNm4 = Label(root, text= "KN.m", font = 'Calibri 10', fg = 'black')
        kNm4.place(x=465, y =480, anchor = CENTER)

        mmsquare1 = Label(root, text= "mm\u00B2", font = 'Calibri 10', fg = 'black')
        mmsquare1.place(x=188, y =450, anchor = CENTER)

        mmsquare2 = Label(root, text= "mm\u00B2", font = 'Calibri 10', fg = 'black')
        mmsquare2.place(x=463, y =450, anchor = CENTER)

        mmsquare3 = Label(root, text= "mm\u00B2", font = 'Calibri 10', fg = 'black')
        mmsquare3.place(x=463, y =420, anchor = CENTER)

        mmsquare4 = Label(root, text= "mm\u00B2", font = 'Calibri 10', fg = 'black')
        mmsquare4.place(x=188, y =420, anchor = CENTER)

        #Buttons

        CalculateButton = Button(root, text= "Calculate", font = 'Calibri 14 bold', fg = 'black', command = calculate, relief = SOLID)
        CalculateButton.place(x=275, y =580, anchor = CENTER)

        ClearButton = Button(root, text= "Clear", font = 'Calibri 12 bold', fg = 'black', height = 1, command = clear, relief = GROOVE)
        ClearButton.place(x=275, y =620, anchor = CENTER)

        #Entries

        #f'c
        e1 = Entry(root, width =8, justify = 'center')
        e1.place(x=43, y =73)

        #fy
        e2 = Entry(root,width =8, justify = 'center')
        e2.place(x=43, y =103)

        #width
        e3 = Entry(root,width =8, justify = 'center')
        e3.place(x=43, y =133)

        #depth
        e4 = Entry(root,width =8, justify = 'center')
        e4.place(x=43, y =163)

        #Mu+
        e6 = Entry(root, width =8, justify = 'center')
        e6.place(x=43, y =190)

        #Mu-
        e7 = Entry(root, width =8, justify = 'center')
        e7.place(x=43, y =220)

        #topcover
        e5 = Entry(root,width =8, justify = 'center')
        e5.place(x=130, y =290)

        #bottomcover
        e12 = Entry(root,width =8, justify = 'center')
        e12.place(x=130, y =320)

        #sidecover
        e13 = Entry(root,width =8, justify = 'center')
        e13.place(x=130, y =350)

        #Capacity for Positive Moment
        e8 = Entry(root,width =8, justify = 'center')
        e8.place(x=145, y =480, anchor = CENTER)

        #Result for Positive Moment
        e9 = Entry(root, width =38, font = 'Calibri 8', fg = 'red', justify = 'center')
        e9.place(x=135, y =540, anchor = CENTER)

        #Result for Negative Moment
        e10 = Entry(root, width =38, font = 'Calibri 8', fg = 'red', justify = 'center')
        e10.place(x=410, y =540, anchor = CENTER)

        #Capacity for Negative Moment
        e11 = Entry(root,width =8, justify = 'center')
        e11.place(x=420, y =480, anchor = CENTER)

        #Negative D/C Ratio
        e14 = Entry(root,width =8, justify = 'center')
        e14.place(x=420, y =510, anchor = CENTER)

        #Positive D/C Ratio
        e15 = Entry(root,width =8, justify = 'center')
        e15.place(x=145, y =510, anchor = CENTER)

        #Positive Area of Steel Provided
        e16 = Entry(root,width =8, justify = 'center')
        e16.place(x=145, y =450, anchor = CENTER)

        #Negative Area of Steel Provided
        e17 = Entry(root,width =8, justify = 'center')
        e17.place(x=420, y =450, anchor = CENTER)

        #Positive Area of Steel Required
        e18 = Entry(root,width =8, justify = 'center')
        e18.place(x=145, y =420, anchor = CENTER)

        #Negative Area of Steel Required
        e19 = Entry(root,width =8, justify = 'center')
        e19.place(x=420, y =420, anchor = CENTER)

        e8.config(state='readonly')
        e9.config(state='readonly')
        e10.config(state='readonly')
        e11.config(state='readonly')
        e14.config(state='readonly')
        e15.config(state='readonly')
        e16.config(state='readonly')
        e17.config(state='readonly')
        e18.config(state='readonly')
        e19.config(state='readonly')

        #ToolTips

        CreateToolTip(e1, 'Compressive Strength of Concrete')
        CreateToolTip(e2, 'Tensile Strength of Steel')
        CreateToolTip(e3, 'Beam Width')
        CreateToolTip(e4, 'Beam Depth')
        CreateToolTip(e5, 'Top Clear Cover')
        CreateToolTip(e6, 'Factored Positive Moment')
        CreateToolTip(e7, 'Factored Negative Moment in Absolute Value')
        CreateToolTip(e8, 'Section Capacity for Positive Moment')
        CreateToolTip(e9, 'Calculation Results for Positive Moment')
        CreateToolTip(e10, 'Calculation Results for Negative Moment')
        CreateToolTip(e11, 'Section Capacity for Negative Moment')
        CreateToolTip(e12, 'Bottom Clear Cover')
        CreateToolTip(e13, 'Side Clear Cover')
        CreateToolTip(e14, 'Demand over Capacity Ratio for Negative Moment')
        CreateToolTip(e15, 'Demand over Capacity Ratio for Positive Moment')
        CreateToolTip(e16, 'Provided Area of Steel for Positive Moment')
        CreateToolTip(e17, 'Provided Area of Steel for Negative Moment')
        CreateToolTip(e18, 'Required Area of Steel for Positive Moment')
        CreateToolTip(e19, 'Required Area of Steel for Negative Moment')


units = [
"Imperial",
"Metric"
]


unitbox = ttk.Combobox(root, value = units, width =11, justify = 'center')
unitbox.current(0)
unitbox.place(x=5, y = 35)
unitbox.config(state='readonly')
unitbox.bind("<<ComboboxSelected>>", design)
unitbox.bind("<FocusIn>", defocus)


def on_close():
    response=messagebox.askyesno('Exit','Are you sure you want to exit?')
    if response:
        root.destroy()

root.protocol('WM_DELETE_WINDOW', on_close)

root.mainloop()