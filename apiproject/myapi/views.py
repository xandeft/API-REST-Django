from rest_framework.response import Response
from .models import ContaCorrente
from .serializers import ContaSerializer
from rest_framework.decorators import api_view

# Create your views here.



@api_view(['GET'])
def accountList(request):
    accounts = ContaCorrente.objects.all()
    serializer = ContaSerializer(accounts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def accountDetail(request, pk):
    account = ContaCorrente.objects.get(accountNumber=pk)
    serializer = ContaSerializer(account, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createAccount(request):
    serializer = ContaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response('Número de conta já existente!')

@api_view(['PUT'])
def depositMoney(request, pk, value):
    account = ContaCorrente.objects.get(accountNumber=pk)
    validatorAccount = dict(request.data)['accountNumber'][0]
    if (validatorAccount == pk):
        valueInAccount = int(account.balance)
        account.balance = str(valueInAccount + value)
        serializer = ContaSerializer(instance=account, data=request.data)

        if (serializer.is_valid()):
            serializer.save()
        return Response(serializer.data)
    
    else:
        return Response('Dados Inválidos!')

@api_view(['PUT'])
def debitMoney(request, pk, value):
    account = ContaCorrente.objects.get(accountNumber=pk)
    valueInAccount = int(account.balance)
    validatorAccount = dict(request.data)['accountNumber'][0]
    if (valueInAccount >= value and validatorAccount == pk):
        account.balance = str(valueInAccount - value)
        serializer = ContaSerializer(instance=account, data=request.data)

        if (serializer.is_valid()):
            serializer.save()
        return Response(serializer.data)
    
    elif (validatorAccount != pk):
        return Response('Dados Inválidos!')
    else:
        return Response('Saldo Insuficiente!')

@api_view(['DELETE'])
def deleteAccount(request, pk):
    account = ContaCorrente.objects.get(accountNumber=pk)
    account.delete()

    return Response('Deleted')