from django.shortcuts import render
from deep_translator import GoogleTranslator

# Create your views here.
def translator_app(request):
    output_text=""
    input_text=""
    select_input="km" 
    select_output="en"

    if request.method=='POST':
        input_text=request.POST.get('input_text','')
        select_input=request.POST.get('select_input','km')
        select_output=request.POST.get('select_output','en')

        if input_text:
            try:
                output_text=GoogleTranslator(source=select_input,target=select_output).translate(input_text)
            except Exception as e:
                output_text="Error! Cannot Transalte it."

    context={
        'output_text': output_text,
        'input_text': input_text,
        'select_input':select_input,
        'select_output': select_output 
    }
    return render(request,'index.html',context)