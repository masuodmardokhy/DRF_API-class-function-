from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view()
def hello_world(request):
    return Response({"messages":"hello world"})

@api_view(['GET', 'POST'])
def hello(request):
    if request.method == "GET":
        return Response({"messages": "helloword"})
    elif request.method == "POST":
        return Response({"messages": "hello,{}".format(request.data["name"])})

@api_view(["POST"])
def calculator(request):
    try:
        nam1 = request.data["num1"]
        num2 = request.data["num2"]
        apr = request.data["apr"]
    except:
        return Response({"error": "send num1 num2 opr "}, status=status.HTTP_400_BAD_REQUEST)
    else:
        if isinstance(nam1, int) and isinstance(num2, int):
            if apr == 'add':
                return Response({"result": nam1 + num2}, status=status.HTTP_200_OK)
            if apr == 'sub':
                return Response({"result": nam1 - num2}, status=status.HTTP_200_OK)
            if apr == 'div':
                return Response({"result": nam1 / num2}, status=status.HTTP_200_OK)
            if apr == 'mul':
                return Response({"result": nam1 * num2}, status=status.HTTP_200_OK)
            else:
                return Response({"erorr": "send a valid apr"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "send num1 num2 not int "}, status=status.HTTP_400_BAD_REQUEST)


