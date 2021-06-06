from django.shortcuts import render
from django.http import HttpResponse
from .forms import infoForm,IMPREDICTORSCR
import pickle
import numpy as np
from keras.models import load_model
from .funcs import testts,Predict_image
from PIL import Image
from PIL import ImageOps
import io
import urllib,base64
import matplotlib.pyplot as plt
def IMSCR(request):
    context = {}
    mode = 0
    if request.method == "POST":
        form = IMPREDICTORSCR(request.POST,request.FILES)
        if form.is_valid():
            if 'TL' in request.POST:
                model = load_model('Signpredictor/NewModels/TransferLearnedModel.h5')
                mode = 1
            if 'SC' in request.POST:
                model = load_model('Signpredictor/NewModels/SignLanguageModelScratch.h5')
            img = form.cleaned_data['Image']
            ii = Image.open(img)
            
            ui,preds = Predict_image(ii,model)
            plt.figure(figsize=(2.5,2.5))
            plt.imshow(ui, interpolation="bilinear", aspect='auto',cmap='gray')
            fig = plt.gcf()
            buf = io.BytesIO()
            fig.savefig(buf,format ='png')
            buf.seek(0)
            string = base64.b64encode(buf.read())
            uri = 'data:image/png;base64,' + urllib.parse.quote(string)
            print(preds)
            context = {'form':form,'pred':preds,'img':uri,'mode':mode}
            return render(request,'ImagePredictor.html',context=context)    
    else:
        form = IMPREDICTORSCR()
        context = {'form':form}
        return render(request,'ImagePredictor.html',context=context)

def description(request):
    return render(request,'des.html')