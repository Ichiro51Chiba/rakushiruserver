from django.shortcuts import render

# Create your views here.
class UserViewSet(viewset.ModelViewSet):
  
  
  def create(self, request):
    print(request.data)
    company_id = request.data.get("company_id", None)
    email = request.data.get("email", None)
    
    
    user_manager = UserManager()
    user_manager.create_user(email, password, compnay=company)
