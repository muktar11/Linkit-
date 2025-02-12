from django.shortcuts import render
from django.http import JsonResponse
<<<<<<< HEAD
from .models import (
    CustomUser,Activity, CashWithdraw,
     Coin, Exchange, Message, Video,
     HomePage, OnlineShop, CustomerPurchase,
     CashRate, PurchaseCoin, WireCoin, DailyCombo,
      DailyComboClaim,

)
from .serializers import  (MyTokenObtainPairSerializer,  
RegisterStaffSerializer,TwoFactorAuthSerializer,
DeleteUserSerializer, CustomUserSerializer,
DailyComboSerializer,
ActivitySerializer,  CashWithdrawSerializer,
CoinSerializer, ExchangeSerializer, MessageSerializer,
VideoSerializer, HomePageSerializer,
OnlineShopSerializer, CustomerPurchaseSerializer,
CashRateSerializer, PurchaseCoinSerializer, WireCoinSerializer,
 DailyComboClaimSerialzier,
)

from datetime import timedelta
from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, ValidationError
=======
from .models import(CustomUser, RatePublish, Profile, 
Publish, CommentPublish, Photo, 
 Video, Invest, Settings, PaymentInfo,
  LikeInvest, RateInvest, CommentInvest) 
from .serializers import  (MyTokenObtainPairSerializer,  ProfileSerializer,
CustomUserProfileSerializer, RegisterStaffSerializer,
ChangePasswordSerializer, UserProfileActivitySerializer,
UserSuggestionWithProfileSerializer,
PublishSerializer, NestedProfileSerializer, 
PhotoSerializer, TwoFactorAuthSerializer, 
InvestRetrieveSerializer, CustomUserSerializer,
VideoSerializer,PublishRetrieveSerializer, 
UserActivitySerializer, InvestSerializer,
SettingsSerializer,LikeInvestSerializer,
RateInvestSerializer, DeleteUserSerializer, 
UserFeedSerializer, FollowSerializer,PaymentInfoSerializer,
CommentInvestSerializer, CommentPublishSerializer
)
>>>>>>> 2b11a5b (first commit)
from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework import generics 
from rest_framework import status
from django.core.paginator import Paginator
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json 
from rest_framework.decorators import api_view, permission_classes
from django.utils.timezone import make_aware
from datetime import datetime
from bs4 import BeautifulSoup
from rest_framework import serializers
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .serializers import ChangePasswordSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser



class MyTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = MyTokenObtainPairSerializer(data=request.data, context={'request': request})
        try:
            serializer.is_valid(raise_exception=True)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        except serializers.ValidationError as e:
            return Response({'detail': e.detail}, status=status.HTTP_400_BAD_REQUEST)
            
      
class TokenRefreshViewCustom(APIView):
    def post(self, request):
        # Get the refresh token from the request
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({"detail": "Refresh token is required."}, status=400)
        try:
            # Check if the refresh token is valid
            refresh = RefreshToken(refresh_token)
            # Generate a new access token
            access_token = str(refresh.access_token)
            return Response({
                "access": access_token,
            })
        except Exception as e:
            print(f"Error: {e}")  # Print the exception for debugging
            return Response({"detail": "Invalid refresh token."}, status=400)

class CustomUserUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
<<<<<<< HEAD
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]  # Change to IsAuthenticated if needed
=======
    serializer_class = CustomUserProfileSerializer
    permission_classes = [IsAuthenticated]
>>>>>>> 2b11a5b (first commit)

    def get_object(self):
        user_id = self.kwargs.get('id')  # Get 'id' from URL kwargs
        return get_object_or_404(CustomUser, id=user_id)
 
class CustomUserListExcludingParamView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]  # Ensure user is authenticated

<<<<<<< HEAD
    def get_queryset(self):
        user_id = self.kwargs.get('user_id')  # Get user ID from URL
        return CustomUser.objects.exclude(id=user_id)

=======
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)  # Allow partial updates
        instance = self.get_object()

        # Preprocess the data to leave fields as-is if they are null
        updated_data = request.data.copy()
        for field in ['username', 'email', 'first_name', 'last_name', 'phone', 'image_url', 'two_factor_required']:
            if field in updated_data and updated_data[field] is None:
                updated_data.pop(field)  # Remove null fields to leave them unchanged

        serializer = self.get_serializer(instance, data=updated_data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Serialize the updated instance
        updated_instance_serializer = self.get_serializer(instance)
        return Response({
            'message': 'Profile updated successfully',
            'updated_data': updated_instance_serializer.data
        }, status=status.HTTP_200_OK)
>>>>>>> 2b11a5b (first commit)
        
# Delete User View
class CustomUserDeleteView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return get_object_or_404(CustomUser, id=self.request.user.id)
    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class RegisterStaffView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterStaffSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print('data', serializer)
        if not serializer.is_valid():
            # Return detailed validation errors
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                'message': 'User registered successfully',
                'user': RegisterStaffSerializer(user).data,
                'access_token': access_token,
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ChangePasswordView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, user_id, *args, **kwargs):
        # Fetch user by ID
        user = get_object_or_404(CustomUser, id=user_id)

        # Serialize and validate the data
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response({'detail': _("Password changed successfully.")}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

<<<<<<< HEAD
=======
class FollowersFollowingView(APIView):
    def get(self, request, user_id, *args, **kwargs):
        try:
            # Fetch the CustomUser using the provided user_id
            user = CustomUser.objects.get(id=user_id)

            # Fetch the Profile associated with this user
            profile = Profile.objects.get(parent=user)

            # Serialize the profile data
            serializer = FollowSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def get_channel_id(request):
    try:
        queryset = Channel.objects.all()
        serializer = ChannelSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
    except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> 2b11a5b (first commit)

@api_view(['POST'])
@permission_classes([AllowAny]) 
def create_activity(request):
    try:
        queryset = Activity.objects.all()
        serializer = ActivitySerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
    except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

<<<<<<< HEAD

@api_view(['POST'])
@permission_classes([AllowAny]) 
def create_cashwithdraw(request, user):
=======
@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def get_profile(request, pk):
>>>>>>> 2b11a5b (first commit)
    try:
        data = request.data.copy()
        data['user'] = user 
        # Deserialize and validate the data
        serializer = CashWithdrawSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        # Save the new message
        serializer.save()
        # Return the created message
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
    except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)


<<<<<<< HEAD
@api_view(['POST'])
@permission_classes([AllowAny])
def create_message(request, user, receiver):
    try:
        # Add the user_id to the data payload
        data = request.data.copy()
        data['user'] = user
        data['receiver'] = receiver
        
        # Deserialize and validate the data
        serializer = MessageSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        
        # Save the new message
        serializer.save()
        
        # Return the created message
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    except AuthenticationFailed as auth_error:
        # Handle expired or invalid token
        print('Authentication error:', auth_error)
        return Response(
            {"detail": "Token expired. Please refresh your token"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    
    except ValidationError as e:
        # Handle validation errors
        print("Validation error:", e.detail)
        return Response(
            {"detail": e.detail},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    except Exception as e:
        # Handle any other exceptions
        print("Unexpected error:", str(e))
        return Response(
            {"detail": "An unexpected error occurred."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
=======

@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def get_user(request, pk):
    try:
        user = CustomUser.objects.get(id=pk)
        serializer = CustomUserSerializer(user, many=False, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Profile.DoesNotExist:
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except AuthenticationFailed as auth_error:
                return Response({"detail": "Token expired. Please refresh your token."},status=status.HTTP_401_UNAUTHORIZED)
    except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def get_user_profile(request, pk):
        try:
            user = CustomUser.objects.get(id=pk)        
            # Fetch related data
            publishes = Publish.objects.filter(parent=user)
            investments = Invest.objects.filter(parent=user)     
            # Fetch followers and following from the user's profile
            profile = user.profile  # Assuming the user has a profile
            # Prepare data for serialization
            data = {
                'publishes': publishes,
                'investments': investments,
            }
            # Serialize the data with context and many=True
            serializer = UserProfileActivitySerializer(
                data,
                context={'request': request, 'user': user},
                many=False  # No need for `many=True` here because the data is a dictionary
            )
            return Response(serializer.data)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> 2b11a5b (first commit)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_message_for_user(request, id):
    try:
        queryset = Message.objects.filter(user=id)  # Assuming user_id is the field
        if not queryset.exists():
            return Response({"detail": "No messages found for this user."}, status=status.HTTP_404_NOT_FOUND)
        serializer = MessageSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

<<<<<<< HEAD
=======

class FollowUnfollowRetrieveView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, parent_id, id):
        try:
            # Get the current user's profile using parent_id
            current_user_profile = Profile.objects.get(user_id=parent_id)
            # Get the target user's profile
            target_user_profile = Profile.objects.get(_id=id)
            # Check if current user is trying to follow/unfollow themselves
            
            if target_user_profile in current_user_profile.following.all():
                # Unfollow the user
                current_user_profile.following.remove(target_user_profile)
                target_user_profile.followers.remove(current_user_profile)
                return Response({"detail": "Unfollowed successfully."}, status=status.HTTP_200_OK)
            else:
                # Follow the user
                current_user_profile.following.add(target_user_profile)
                target_user_profile.followers.add(current_user_profile)
                return Response({"detail": "Followed successfully."}, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)

class FollowersFollowingRetrieveView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        try:
            # Get the user's profile
            user_profile = Profile.objects.get(user_id=user_id)

            followers = user_profile.followers.all()
            following = user_profile.following.all()

            followers_data = ProfileSerializer(followers, many=True).data
            following_data = ProfileSerializer(following, many=True).data

            return Response({
                "followers": followers_data,
                "following": following_data,
            }, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)

class ProfileSearchView(APIView):
    permission_classes = [IsAuthenticated]
>>>>>>> 2b11a5b (first commit)


@api_view(['GET'])
def get_all_urls(request):
    try:
        urls = Video.objects.all() # Retrieve only 'id' and 'url'
        urlsserilizer = VideoSerializer(urls, many=True)
        return Response(urlsserilizer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_all_users(request):
    try:
        users = CustomUser.objects.all()  # Retrieve all users
        userserializer = CustomUserSerializer(users, many=True)  # Serialize data
        return Response(userserializer.data, status=status.HTTP_200_OK)  # Use .data to return JSON
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
def get_all_coin(request):
    try:
        coin  = Coin.objects.all()  # Retrieve specific fields
        coinserilizer = CoinSerializer(coin, many=True)
        return Response(coinserilizer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_all_exchange(request):
    try:
        users = CashRate.objects.all()  # Retrieve specific fields
        usersserilizer = CashRateSerializer(users, many=True)
        return Response(usersserilizer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
@permission_classes([AllowAny])
def get_cashwithdraw_for_user(request, id):
    try:
        queryset = CashWithdraw.objects.filter(user=id)  # Assuming user_id is the field
        if not queryset.exists():
            return Response({"detail": "No messages found for this user."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CashWithdrawSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([AllowAny]) 
def get_message_for_all(request):
    try:
        queryset = Message.objects.all()
        serializer = MessageSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([AllowAny]) 
def get_cashwithdraw_for_all(request):
    try:
        queryset = CashWithdraw.objects.all()
        serializer = CashWithdrawSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

     

class IncreaseCoinsView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = request.user
        coins_earned = 1
        user.coins += coins_earned
        user.save()

        # Record the activity
        activity = Activity.objects.create(
            user=user,
            activity_type='tap',
            coins_earned=coins_earned
        )

        # Serialize and return the activity
        activity_serializer = ActivitySerializer(activity)
        return Response({
            "message": "Coins increased successfully",
            "user": UserSerializer(user).data,
            "activity": activity_serializer.data
        }, status=status.HTTP_201_CREATED)

class WatchVideoEarnCoinsView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = request.user
        coins_earned = 5
        user.coins += coins_earned
        user.save()

        # Record the activity
        activity = Activity.objects.create(
            user=user,
            activity_type='video_watch',
            coins_earned=coins_earned
        )

        # Serialize and return the activity
        activity_serializer = ActivitySerializer(activity)
        return Response({
            "message": "Coins earned by watching a video",
            "user": UserSerializer(user).data,
            "activity": activity_serializer.data
        }, status=status.HTTP_201_CREATED)

class RedeemCoinView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = request.user
        coin_code = request.data.get("coinCode")

        try:
            # Find the coin by code
            coin = Coin.objects.get(code=coin_code)
        except Coin.DoesNotExist:
            return Response({"message": "Coin code not found"}, status=status.HTTP_404_NOT_FOUND)



        # Check if the coin has expired
        if coin.expiry_date and coin.expiry_date < now():
            return Response({"message": "Coin code has expired"}, status=status.HTTP_400_BAD_REQUEST)

        # Add the coin value to the user's coin count
        user.coins += coin.value
        user.save()

        return Response({
            "message": "Coin redeemed successfully",
            "user": UserSerializer(user).data,
            "coin_value": coin.value
        }, status=status.HTTP_200_OK)

# Create or Update a Coin
class CreateCoinView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = CoinSerializer(data=data)
            if serializer.is_valid():
                # Delete expired coins
                deleted_count = Coin.delete_expired_coins()

                # Create a new coin
                coin = serializer.save()
                return Response({
                    'message': f'Coin created successfully, {deleted_count} expired coins were deleted',
                    'data': CoinSerializer(coin).data
                }, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({
                'message': 'Error creating coin',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CreateDailyComboView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = DailyComboSerializer(data=data)
            serializer.is_valid(raise_exception=True)  # Fixed typo
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ValidationError as e:
            # Handle validation errors
            return Response(
                {"detail": e.detail},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            # Handle any other exceptions
            print("Unexpected error:", str(e))
            return Response(
                {"detail": "An unexpected error occurred."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )



<<<<<<< HEAD
class DailyComboClaimView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, user_id, combo_id):
        user = get_object_or_404(CustomUser, id=user_id)
        combo = get_object_or_404(DailyCombo, id=combo_id)

        # Check if the user has already claimed this combo
        claim = DailyComboClaim.objects.filter(user=user, combo=combo).first()
        if claim and claim.is_claimed:
            return Response({"message": "You have already claimed this combo."}, status=status.HTTP_400_BAD_REQUEST)
        # If no claim exists, create a new one
        if not claim:
            claim = DailyComboClaim(user=user, combo=combo)
        # Add accomplishment_value to the user's coins
        user.coins += combo.accomplishment_value
        user.save()
        # Mark the claim as claimed
        claim.is_claimed = True
        claim.save()
        return Response({"message": "Combo claimed successfully!", "new_coins": user.coins}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny]) 
def get_daily_combo_for_all(request):
    try:
        queryset = DailyCombo.objects.all()
        serializer = DailyComboSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)



# Delete a Coin by ID
class DeleteCoinView(APIView):
    def delete(self, request, id):
        try:
            coin = Coin.objects.filter(id=id).first()
            if not coin:
                return Response({'message': 'Coin not found'}, status=status.HTTP_404_NOT_FOUND)

            coin.delete()
            return Response({'message': 'Coin deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': 'Error deleting coin',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Retrieve All Coins
class GetAllCoinsView(APIView):
    def get(self, request):
        try:
            coins = Coin.objects.all()
            serializer = CoinSerializer(coins, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': 'Error retrieving coins',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Fetch all unprocessed requests
class UnprocessedRequestsView(generics.ListAPIView):
    queryset = CashWithdraw.objects.filter(is_processed=False)
    serializer_class = CashWithdrawSerializer


# Fetch all processed requests
class ProcessedRequestsView(generics.ListAPIView):
    queryset = CashWithdraw.objects.filter(is_processed=True)
    serializer_class = CashWithdrawSerializer




class DailyRewardView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, user_id):
        try:
            user = get_object_or_404(CustomUser, id=user_id)
            homepage, created = HomePage.objects.get_or_create(user=user)
            #homepage = get_object_or_404(HomePage, user=user)

            # Add 100 coins for daily reward
            user.coins += 100
            user.save()

            homepage.daily_reward = 100  # Update the daily reward value
            homepage.save()

            # Return the updated homepage data
            serializer = HomePageSerializer(homepage)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class DailyComboView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, user_id):
        try:
            user = get_object_or_404(CustomUser, id=user_id)
            homepage, created = HomePage.objects.get_or_create(user=user)
            # Add 50 coins for daily combo
            user.coins += 50
            user.save()
            homepage.daily_combo = 50  # Update the daily combo value
            homepage.save()
            # Return the updated homepage data
            serializer = HomePageSerializer(homepage)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except AuthenticationFailed as auth_error:
                    # Handle expired or invalid token
                    print("Authentication error:", auth_error)
                    return Response(
                        {"detail": "Token expired. Please refresh your token."},
                        status=status.HTTP_401_UNAUTHORIZED,
                    )        
class DailyCipherView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, user_id):
        try:
            user = get_object_or_404(CustomUser, id=user_id)
            homepage, created = HomePage.objects.get_or_create(user=user)
            # Add 10 coins for daily cipher
            user.coins += 10
            user.save()
            homepage.daily_cipher = 10  # Update the daily cipher value
            homepage.save()
            # Return the updated homepage data
            serializer = HomePageSerializer(homepage)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )        
# Update the status of a request to processed
class ProcessRequestView(APIView):
    permission_classes = [AllowAny]
    def patch(self, request, pk):
        try:
            cash_withdraw = CashWithdraw.objects.get(pk=pk)
            cash_withdraw.is_processed = True
            cash_withdraw.save()
            serializer = CashWithdrawSerializer(cash_withdraw)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except CashWithdraw.DoesNotExist:
            return Response({"message": "Request not found"}, status=status.HTTP_404_NOT_FOUND)


# Create a new cash withdrawal request
class CreateCashWithdrawView(generics.CreateAPIView):
    serializer_class = CashWithdrawSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)  # Associate the logged-in user
        except AuthenticationFailed as auth_error:
                    # Handle expired or invalid token
                    print("Authentication error:", auth_error)
                    return Response(
                        {"detail": "Token expired. Please refresh your token."},
                        status=status.HTTP_401_UNAUTHORIZED,
                    )        

from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# Fetch all cash withdrawal requests for a user
class UserCashWithdrawalsView(generics.ListAPIView):
    serializer_class = CashWithdrawSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        try:
            user_id = self.kwargs.get('user_id')
            return CashWithdraw.objects.filter(user_id=user_id)
        except AuthenticationFailed as auth_error:
                    # Handle expired or invalid token
                    print("Authentication error:", auth_error)
                    return Response(
                        {"detail": "Token expired. Please refresh your token."},
                        status=status.HTTP_401_UNAUTHORIZED,
                    )        
    def post(self, request, user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
            print('user', user)
            data = request.data
            print('data', data)

            cashwithdrawactivity = CashWithdraw.objects.create(
                paypal_email_address=data.get('paypal_email'),
                
                amount_to_send=data.get('amount'),
                currency=data.get('currency'),
                recepient_name=data.get('recepient_name'),
                user=user
            )

            serializer = self.get_serializer(cashwithdrawactivity)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )


# Create or Update a Coin
class CreateOrUpdateCoinView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            # Extract data from the request
            code = request.data.get('code')
            value = request.data.get('value')
            expiry_date = request.data.get('expiry_date')

            # Delete all existing coins
            Coin.objects.all().delete()

            # Create a new coin
            coin = Coin.objects.create(
                code=code,
                value=value,
                expiry_date=expiry_date
            )

            serializer = CoinSerializer(coin)
            return Response(
                {
                    "message": "Coin created successfully, existing coins were deleted",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as e:
            print(e)
            return Response(
                {"message": "Error creating coin", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


# Delete a Coin by ID
class DeleteCoinView(APIView):
    permission_classes = [AllowAny]
    def delete(self, request, pk):
        try:
            coin = Coin.objects.filter(id=pk).first()
            if not coin:
                return Response({"message": "Coin not found"}, status=status.HTTP_404_NOT_FOUND)

            coin.delete()
            return Response({"message": "Coin deleted successfully"}, status=status.HTTP_200_OK)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as e:
            return Response(
                {"message": "Error deleting coin", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


# Retrieve All Coins
class GetAllCoinsView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            coins = Coin.objects.all()
            serializer = CoinSerializer(coins, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as e:
            return Response(
                {"message": "Error fetching coins", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

class CreateOrUpdateExchangeView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            # Extract data from the request
            data = request.data
            print('data', data)
            currencytype = request.data.get('currencytype')
            value = request.data.get('value')
            expiry_date = request.data.get('expiry_date')
            

            # Validate required fields
            if not currencytype or not value or not expiry_date:
                return Response(
                    {"message": "currencytype, value, and expiry_date are required."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Convert expiry_date to timezone-aware datetime
            
            try:
                expiry_date = make_aware(datetime.fromisoformat(expiry_date))
            except ValueError:
                return Response(
                    {"message": "Invalid expiry_date format. Use ISO 8601 format."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Delete all existing exchange rates
            Exchange.objects.all().delete()

            # Create a new exchange rate
            exchange = Exchange.objects.create(
                currencytype=currencytype,
                value=value,
                expiry_date=expiry_date,
            
            )

            serializer = ExchangeSerializer(exchange)
            return Response(
                {
                    "message": "Exchange created successfully, existing rates were deleted",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        except Exception as e:
            print(e)
            return Response(
                {"message": "Error creating exchange", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

# Delete an Exchange by ID
class DeleteExchangeView(APIView):
    permission_classes = [AllowAny]
    def delete(self, request, pk):
        try:
            exchange = Exchange.objects.filter(id=pk).first()
            if not exchange:
                return Response({"message": "Exchange not found"}, status=status.HTTP_404_NOT_FOUND)

            exchange.delete()
            return Response({"message": "Exchange deleted successfully"}, status=status.HTTP_200_OK)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as e:
            return Response(
                {"message": "Error deleting exchange", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


# Retrieve All Exchanges
class GetAllExchangesView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            exchanges = Exchange.objects.all()
            serializer = ExchangeSerializer(exchanges, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as e:
            return Response(
                {"message": "Error fetching exchanges", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
# Create a new message
class CreateMessageView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        user_id = request.data.get('user_id')
        content = request.data.get('content')

        try:
            # Check if the user exists
            user = User.objects.filter(id=user_id).first()
            if not user:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

            # Create the message
            message = Message.objects.create(user=user, content=content)
            serializer = MessageSerializer(message)
            return Response({'message': serializer.data}, status=status.HTTP_201_CREATED)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as e:
            return Response({'error': 'An error occurred while creating the message', 'details': str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Retrieve messages by user_id
class GetMessagesByUserIdView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, user_id):
        try:
            # Check if the user exists
            user = User.objects.filter(id=user_id).first()
            if not user:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

            # Retrieve messages for the user
            messages = Message.objects.filter(user=user).order_by('-timestamp')
            serializer = MessageSerializer(messages, many=True)
            return Response({'messages': serializer.data}, status=status.HTTP_200_OK)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as e:
            return Response({'error': 'An error occurred while retrieving messages', 'details': str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Retrieve all messages
class GetAllMessagesView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            messages = Message.objects.all().order_by('-timestamp')
            serializer = MessageSerializer(messages, many=True)
            return Response({'messages': serializer.data}, status=status.HTTP_200_OK)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as e:
            return Response({'error': 'An error occurred while retrieving messages', 'details': str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Retrieve all messages sent to a specific user
class GetAllMessagesSentToUserView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, user_id):
        try:
            # Check if the user exists
            user = User.objects.filter(id=user_id).first()
            if not user:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

            # Retrieve all messages sent to the specific user
            messages = Message.objects.filter(user=user).order_by('-timestamp')
            serializer = MessageSerializer(messages, many=True)
            return Response({'messages': serializer.data}, status=status.HTTP_200_OK)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as e:
            return Response({'error': 'An error occurred while retrieving messages', 'details': str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Sanitize URL
def sanitize_url(raw_url):
    soup = BeautifulSoup(raw_url, 'html.parser')
    anchor_tag = soup.find('a', href=True)
    return anchor_tag['href'] if anchor_tag else raw_url

# Create or Update Video
class CreateYoutubeVideoView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            url = request.data.get('url')
            platform = request.data.get('platform')

            # Sanitize URL
            url = sanitize_url(url)

            # Validate platform
            valid_platforms = ['YouTube', 'TikTok', 'FaceBook', 'Twitter', 'Instagram']
            if platform not in valid_platforms:
                return Response(
                    {'message': 'Invalid platform. Please provide one of the following: YouTube, TikTok, Twitter, Instagram'},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Delete existing video for the platform
            Video.objects.filter(platform=platform).delete()

            # Create a new video
            video = Video.objects.create(url=url, platform=platform)
            serializer = VideoSerializer(video)

            return Response(
                {
                    'message': f'Video for platform {platform} created successfully. Existing videos for this platform were deleted.',
                    'data': serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as e:
            print(e)
            return Response(
                {'message': 'Error creating video', 'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class RetrieveYoutubeVideoView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, platform):
        try:
            # Validate platform
            valid_platforms = ['YouTube', 'TikTok', 'FaceBook', 'Twitter', 'Instagram']
            if platform not in valid_platforms:
                return Response(
                    {'message': 'Invalid platform. Please provide one of the following: YouTube, TikTok, Twitter, Instagram'},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # Retrieve the video for the specified platform
            video = Video.objects.filter(platform=platform).first()
            if not video:
                return Response(
                    {'message': f'No video found for platform {platform}'},
                    status=status.HTTP_404_NOT_FOUND,
                )
            serializer = VideoSerializer(video)
            return Response(
                {'message': f'Video for platform {platform} retrieved successfully.', 'data': serializer.data},
                status=status.HTTP_200_OK,
            )
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )                            
        except Exception as e:
            print(e)
            return Response(
                {'message': 'Error retrieving video', 'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
# Delete Video by ID
class DeleteYoutubeVideoView(APIView):
    permission_classes = [AllowAny]
    def delete(self, request, pk):
        try:
            video = Video.objects.filter(pk=pk).first()
            if not video:
                return Response(
                    {'message': 'Video not found'},
                    status=status.HTTP_404_NOT_FOUND,
                )

            video.delete()
            return Response({'message': 'Video deleted successfully'}, status=status.HTTP_200_OK)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as e:
            return Response(
                {'message': 'Error deleting video', 'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

# Get All Videos
class GetAllYoutubeVideosView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            videos = Video.objects.all()
            serializer = VideoSerializer(videos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

# Create OnlineShop
class CreateOnlineShopView(generics.CreateAPIView):
    queryset = OnlineShop.objects.all()
    serializer_class = OnlineShopSerializer
    permission_classes = [AllowAny]


class CreateCashRateView(generics.CreateAPIView):
    queryset = CashRate.objects.all()
    serializer_class = CashRateSerializer
    permission_classes = [AllowAny]

class CreatePurchaseCoinView(generics.CreateAPIView):
    queryset = PurchaseCoin.objects.all()
    serializer_class = PurchaseCoinSerializer
    permission_classess = [AllowAny]

class CustomerPurcahseRetrieve(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        purchase = CustomerPurchase.objects.all()
        serializer = CustomerPurchaseSerializer(purchase, many=True, context={'request': request})
        return Response(serializer.data)

class CreateWireCoinView(generics.CreateAPIView):
    serializer_class = WireCoinSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')  # Get user ID from URL param
        recipient_id = request.data.get('recepient')
        no_of_coins = int(request.data.get('no_of_coins', 0))

        # Get sender (user)
        user = get_object_or_404(CustomUser, id=user_id)

        # Get recipient
        recipient = get_object_or_404(CustomUser, id=recipient_id)

        # Ensure user has enough coins
        if user.coins < no_of_coins:
            return Response({'error': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)

        # Deduct coins from sender and add to recipient
        user.coins -= no_of_coins
        recipient.coins += no_of_coins
        user.save()
        recipient.save()

        # Create WireCoin record
        wire_coin = WireCoin.objects.create(
            user=user,
            recepient=recipient,
            no_of_coins=no_of_coins,
            is_paid=True  # Mark transaction as paid
        )

        return Response(WireCoinSerializer(wire_coin).data, status=status.HTTP_201_CREATED)
        
# Retrieve Single OnlineShop
class RetrieveOnlineShopView(generics.RetrieveAPIView):
    queryset = OnlineShop.objects.all()
    serializer_class = OnlineShopSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'  # Get shop by ID

class RetrieveCashRateView(generics.RetrieveAPIView):
    queryset = CashRate.objects.all()
    serializer_class = CashRateSerializer
    permission_classes = [AllowAny]
    lookup_fields = 'pk'


class RetrievePurchaseCoinView(generics.RetrieveAPIView):
    queryset = PurchaseCoin.objects.all()
    serializer_class = PurchaseCoinSerializer
    permission_classes = [AllowAny]
    lookup_fields = 'pk'

class RetrieveAllOnlineShopView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        shops = OnlineShop.objects.all()
        serializer = OnlineShopSerializer(shops, many=True,  context={'request': request})
        return Response(serializer.data)


class RetrieveAllCashRateView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        cashrate = CashRate.objects.all().order_by('-timestamp')
        serializer = CashRateSerializer(cashrate, many=True)
        return Response(serializer.data)


class RetirevePurcahseCoinView(APIView):
    permission_classes =  [AllowAny]
    def get(self, request):
        purchase = PurchaseCoin.objects.filter(is_paid=False)
        serializer =  PurchaseCoinSerializer(purchase, many=True)
        return Response(serializer.data)


class RetrieveWireCoinView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        wirecoin = WireCoin.objects.all()
        serializer = WireCoinSerializer(wirecoin, many=True)
        return Response(serializer.data)
# Update OnlineShop
class UpdateOnlineShopView(generics.UpdateAPIView):
    queryset = OnlineShop.objects.all()
    serializer_class = OnlineShopSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'  # Update by ID


class UpdateCashRateView(generics.UpdateAPIView):
    queryset = CashRate.objects.all()
    serializer_class = CashRateSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'
# Create Purchase
class CreatePurchaseView(generics.CreateAPIView):
    queryset = CustomerPurchase.objects.all()
    serializer_class = CustomerPurchaseSerializer
    permission_classes = [AllowAny]

# Get Purchases by User ID
class GetPurchaseByUserView(generics.ListAPIView):
    serializer_class = CustomerPurchaseSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return CustomerPurchase.objects.filter(user_id=user_id)

# Update Purchase
class UpdatePurchaseView(generics.UpdateAPIView):
    queryset = CustomerPurchase.objects.all()
    serializer_class = CustomerPurchaseSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'  # Update by ID
=======

class UserActivityView(APIView):
   # permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            user = CustomUser.objects.get(id=pk)        
            # Fetch related data
            publishes = Publish.objects.filter(parent=user)
            likes = LikePublish.objects.filter(user=user)
            ratings = RatePublish.objects.filter(user=user)
            investments = Invest.objects.filter(parent=user)     
            # Fetch followers and following from the user's profile
            profile = user.profile  # Assuming the user has a profile
            # Prepare data for serialization
            data = {
                'publishes': publishes,
                'likes': likes,
                'ratings': ratings,
                'investments': investments,
            }
            # Serialize the data with context and many=True
            serializer = UserActivitySerializer(
                data,
                context={'request': request, 'user': user},
                many=False  # No need for `many=True` here because the data is a dictionary
            )
            return Response(serializer.data)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        item_type = request.data.get('type')
        item_id = request.data.get('id')
        updated_data = request.data.get('updated_data')
        if not all([item_type, item_id, updated_data]):
            return Response(
                {"error": "Missing type, id, or updated_data in the request."},
                status=400,
            )
        try:
            if item_type == 'publishes':
                item = Publish.objects.get(id=item_id)
            elif item_type == 'likes':
                item = LikePublish.objects.get(id=item_id)
            elif item_type == 'ratings':
                item = RatePublish.objects.get(id=item_id)
            elif item_type == 'investments':
                item = Invest.objects.get(id=item_id)
            else:
                return Response({"error": "Invalid type provided."}, status=400)

            # Update the fields dynamically
            for key, value in updated_data.items():
                setattr(item, key, value)
            item.save()

            return Response({"success": f"{item_type} item updated successfully."})
        except Exception as e:
            return Response({"error": str(e)}, status=404)

        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        """
        Handles deleting an item.
        Expected input:
        - type: Type of item ('publishes', 'likes', 'ratings', 'investments')
        - id: ID of the item to delete
        """
        item_type = request.data.get('type')
        item_id = request.data.get('id')

        if not all([item_type, item_id]):
            return Response(
                {"error": "Missing type or id in the request."},
                status=400,
            )

        try:
            if item_type == 'publishes':
                item = Publish.objects.get(id=item_id)
            elif item_type == 'likes':
                item = LikePublish.objects.get(id=item_id)
            elif item_type == 'ratings':
                item = RatePublish.objects.get(id=item_id)
            elif item_type == 'investments':
                item = Invest.objects.get(id=item_id)
            else:
                return Response({"error": "Invalid type provided."}, status=400)

            item.delete()
            return Response({"success": f"{item_type} item deleted successfully."})
        except Exception as e:
            return Response({"error": str(e)}, status=404)

        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        user_id = self.kwargs.get('pk')  # Get user ID from URL
        try:
            # Debugging: print the ID
            print(f"Looking for Profile with _id: {user_id}")
            profile = Profile.objects.get(_id=user_id)
            return profile
        except Profile.DoesNotExist:
            raise NotFound(detail="User not found.")
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

from django.db.models import Count

class SuggestedUsersView(APIView):
      # Adjust permissions as needed

    def get(self, request, user_id, format=None):
        try:
            # Fetch the current user's profile
            current_user_profile = Profile.objects.get(user_id=user_id)
            current_user = current_user_profile.parent

            # Get the list of users the current user is already following
            already_following_ids = current_user_profile.following.values_list('parent__id', flat=True)

            # Find mutual connections based on the CustomUser model
            mutual_connections = CustomUser.objects.filter(
                profile__followers__parent__id__in=already_following_ids  # Users followed by those the current user follows
            ).exclude(
                id__in=already_following_ids  # Exclude already-followed users
            ).exclude(
                id=current_user.id  # Exclude the current user
            ).annotate(
                mutual_count=Count('profile__followers')  # Count mutual followers
            ).order_by('-mutual_count')  # Sort by mutual connections count

            if mutual_connections.exists():
                serializer = CustomUserProfileSerializer(mutual_connections, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

            # If no mutual connections, find unconnected users
            unconnected_users = CustomUser.objects.exclude(
                id__in=already_following_ids  # Exclude already-followed users
            ).exclude(
                profile__followers=current_user_profile  # Exclude users following the current user
            ).exclude(
                id=current_user.id  # Exclude the current user
            )

            serializer = CustomUserProfile(unconnected_users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Profile.DoesNotExist:
            raise NotFound(detail="Profile not found.")
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SuggestedUsersView(APIView):
    def get(self, request, user_id, format=None):
        try:
            current_user_profile = Profile.objects.get(user_id=user_id)
            current_user = current_user_profile.parent

            already_following_ids = current_user_profile.following.values_list('parent__id', flat=True)

            mutual_connections = CustomUser.objects.filter(
            profile__followers__parent__id__in=already_following_ids
        ).exclude(
            id__in=already_following_ids
        ).exclude(
            id=current_user.id
        ).annotate(
            mutual_count=Count('profile__followers')
        ).order_by('-mutual_count')


            if mutual_connections.exists():
                serializer = CustomUserProfileSerializer(mutual_connections, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

            unconnected_users = CustomUser.objects.exclude(
                id__in=already_following_ids
            ).exclude(
                profile__followers=current_user_profile
            ).exclude(
                id=current_user.id
            ).prefetch_related('profile')  # Use prefetch_related for reverse relation

            serializer = UserSuggestionWithProfileSerializer(unconnected_users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AuthenticationFailed as auth_error:
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Profile.DoesNotExist:
            raise NotFound(detail="Profile not found.")
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProfileFollowersFollowingView(APIView):
    permission_classes = [AllowAny]  # You can adjust permissions as needed

    def get(self, request, user_id, format=None):
        try:
            # Fetch the profile for the given user_id
            profile = Profile.objects.get(user_id=user_id)
            
            # Get the list of followers
            followers = profile.followers.all()
            
            # Get the list of following
            following = profile.following.all()
            
            # Serialize the followers and following lists
            followers_serializer = NestedProfileSerializer(followers, many=True)
            following_serializer = NestedProfileSerializer(following, many=True)
            
            # Return the serialized data
            return Response({
                "followers": followers_serializer.data,
                "following": following_serializer.data
            }, status=status.HTTP_200_OK)

        except Profile.DoesNotExist:
            raise NotFound(detail="Profile not found.")
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


from rest_framework.parsers import MultiPartParser, FormParser
class PublishListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        try:
            # Print the incoming data for debugging
            print("Incoming data:", request.data)

            # Use the serializer to validate and save the data
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            # Print validated data for debugging
            print("Validated data:", serializer.validated_data)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.exceptions import ValidationError
'''
class PublishListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer
    parser_classes = [MultiPartParser, FormParser]
    def create(self, request, *args, **kwargs):
        # Print the incoming data for debugging
        print("Incoming data:", request.data)
        # Use the serializer to validate and save the data
        serializer = self.get_serializer(data=request.data)
        try:
            # Attempt to validate the data
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        # If validation passes, save the object
        self.perform_create(serializer)
        # Print validated data for debugging
        print("Validated data:", serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
'''

class PublishListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer
    parser_classes = [MultiPartParser, FormParser]
    def create(self, request, *args, **kwargs):
        try:
            # Print the incoming data for debugging
            print("Incoming data:", request.data)
            # Use the serializer to validate and save the data
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            # If validation passes, save the object
            self.perform_create(serializer)
            # Print validated data for debugging
            print("Validated data:", serializer.validated_data)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

class PublishDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            # Use prefetch_related to optimize fetching related photos and videos
            publish_instance = Publish.objects.prefetch_related('photos', 'videos').get(pk=pk)
            serializer = PublishRetrieveSerializer(publish_instance, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Publish.DoesNotExist:
            return Response({"error": "Publish not found."}, status=status.HTTP_404_NOT_FOUND)

        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            # Print the incoming data
            print("Incoming data:", request.data)

            # Fetch the Publish instance to be updated
            publish_instance = Publish.objects.prefetch_related('photos', 'videos').get(pk=pk)

            # Serialize and validate the incoming data
            serializer = PublishRetrieveSerializer(
                publish_instance, 
                data=request.data, 
                context={'request': request}, 
                partial=True  # Allows partial updates
            )

            if serializer.is_valid():
                # Save the updated instance
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # If validation fails, return the errors
                print("Validation errors:", serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Publish.DoesNotExist:
            return Response({"error": "Publish not found."}, status=status.HTTP_404_NOT_FOUND)

        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

# View for listing and creating Photo objects related to a Publish
class PhotoListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, publish_id):
        try:
            photos = Photo.objects.filter(publish_id=publish_id)
            serializer = PhotoSerializer(photos, many=True)
            return Response(serializer.data)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
    def post(self, request, publish_id):
        try:
            data = request.data
            data['publish'] = publish_id
            serializer = PhotoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
# View for listing and creating Video objects related to a Publish
class VideoListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, publish_id):
        try:
            videos = Video.objects.filter(publish_id=publish_id)
            serializer = VideoSerializer(videos, many=True)
            return Response(serializer.data)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
    def post(self, request, publish_id):
        try:
            data = request.data
            data['publish'] = publish_id
            serializer = VideoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LikePublish, Publish, CustomUser
'''
# Serializer
class LikePublishSerializer(serializers.ModelSerializer):
    permission_classes = [IsAuthenticated]
    class Meta:
        model = LikePublish
        fields = ['_id', 'parent', 'user', 'likes', 'created_at']

'''

class LikePublishView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, id, pk):
        # Retrieve the user instance
        try:
            user = CustomUser.objects.get(id=id)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Retrieve the publish instance
        try:
            publish = Publish.objects.get(pk=pk)
        except Publish.DoesNotExist:
            return Response({"error": "Publish not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            # Check if the user has already liked the publish
            like, created = LikePublish.objects.get_or_create(
                user=user,
                parent=publish,
            )

            if not created:
                # If the like already exists, remove it (unlike)
                like.delete()
                message = "Like removed"
            else:
                # If the like does not exist, set likes to True and save
                like.likes = True
                like.save()
                message = "Like added"
            # Recalculate the like count after the like/unlike action
            like_count = LikePublish.objects.filter(parent=publish, likes=True).count()
            # Return the response with the updated like count
            return Response({"message": message, "like_count": like_count}, status=status.HTTP_200_OK if not created else status.HTTP_201_CREATED)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

class RatePublishView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, id, pk):
        data = request.data
        try:
            user = CustomUser.objects.get(id=id)
        except CustomUser.DoesNotExist:
            return Response({'error': "User not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            publish = Publish.objects.get(pk=pk)
        except Publish.DoesNotExist:
            return Response({"error": "Publish not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            # Check if the user has already rated the publish
            existing_rate = RatePublish.objects.filter(user=user, parent=publish).first()

            # If a rating exists, delete it to replace with the new one
            if existing_rate:
                existing_rate.delete()
                message = "Previous rating deleted and updated with new rating"
            else:
                message = "Rating successfully created"

            # Create a new rating
            RatePublish.objects.create(
                user=user,
                parent=publish,
                rate=True,
                no_of_rating=data.get('no_of_rating', 0)  # Default to 0 if no value is provided
            )

            # Calculate the total like count for the publish
            like_count = RatePublish.objects.filter(parent=publish).count()

            return Response({
                "message": message,
                "like_count": like_count  # Return the updated like count
            }, status=status.HTTP_201_CREATED)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

class CommentPublishView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id, pk):
        data = request.data
        print('incoming', data)
        try:
            user = CustomUser.objects.get(id=id)
        except CustomUser.DoesNotExist:
            return Response({'error': "User not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            publish = Publish.objects.get(pk=pk)
        except Publish.DoesNotExist:
            return Response({"error": "Publish not found"}, status=status.HTTP_404_NOT_FOUND)

         # Handle photo upload
        photo = request.FILES.get('photo', None)  # Get the photo file if provided

        try:
            # Create a new comment
            comment = CommentPublish.objects.create(
                user=user,
                parent=publish,
                comment=data.get('comment', ''),  # Default to an empty string if no value is provided
                photos=photo if photo else None,
            )

            # Example response with additional data (adjust as needed)
            return Response({
                "message": "Comment successfully created",
                "comment_id": comment._id,
                "comment": comment.comment,
                  "photo_url": comment.photos.url if comment.photos else None,  # Include the photo URL if available
            }, status=status.HTTP_201_CREATED)

        except ValidationError as e:
            # If validation fails, return the error details
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)


class CreateCommentReplyView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        parent_comment_id = kwargs.get('parent_comment_id')  # ID of the comment being replied to
        # Ensure the parent comment exists
        try:
            parent_comment = CommentPublish.objects.get(pk=parent_comment_id)
        except CommentPublish.DoesNotExist:
            return Response(
                {"error": "Parent comment not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        # Add the parent comment to the request data
        data = request.data.copy()
        data['parent_comment'] = parent_comment_id
        # Serialize the data
        serializer = CommentPublishSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Save with the authenticated user
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LikeInvestView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, id, pk):
        # Retrieve the user instance
        try:
            user = CustomUser.objects.get(id=id)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)        
        # Retrieve the invest instance
        try:
            invest = Invest.objects.get(pk=pk)
        except Invest.DoesNotExist:  # Correct the class reference here
            return Response({"error": "Invest not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            # Check if the user has already liked the invest
            like, created = LikeInvest.objects.get_or_create(
                user=user,
                parent=invest,
            )
            if not created:
                # If the like already exists, remove it (unlike)
                like.delete()
                message = "Like removed"
            else:
                # If the like does not exist, set likes to True and save
                like.likes = True
                like.save()
                message = "Like added"
            # Recalculate the like count after the like/unlike action
            like_count = LikeInvest.objects.filter(parent=invest, likes=True).count()
            # Return the response with the updated like count
            return Response({"message": message, "like_count": like_count}, status=status.HTTP_200_OK if not created else status.HTTP_201_CREATED)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)


from django.db.models import Sum, Q, Count, Case, When, IntegerField
'''



class PublishInvestSearchView(APIView):
    def get(self, request):
        query = request.GET.get('query', '')
        if not query:
            return Response({'error': 'Query parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        # Split the query into individual keywords
        keywords = query.split()
        # Annotate Publish objects with a match score
        publish_queryset = Publish.objects.all()
        for keyword in keywords:
            publish_queryset = publish_queryset.annotate(
                match_score=Count(
                    Case(
                        When(Q(title__icontains=keyword) | 
                             Q(author__icontains=keyword) | 
                             Q(organization__icontains=keyword) | 
                             Q(short_description__icontains=keyword), 
                             then=1),
                        output_field=IntegerField()
                    )
                )
            )
        publish_queryset = publish_queryset.order_by('-match_score')
        publish_serializer = PublishRetrieveSerializer(publish_queryset, many=True)
        # Annotate Invest objects with a match score
        invest_queryset = Invest.objects.all()
        for keyword in keywords:
            invest_queryset = invest_queryset.annotate(
                match_score=Count(
                    Case(
                        When(Q(title__icontains=keyword) |
                             Q(description__icontains=keyword) |
                             Q(category__icontains=keyword),
                             then=1),
                        output_field=IntegerField()
                    )
                )
            )
        invest_queryset = invest_queryset.order_by('-match_score')
        invest_serializer = InvestRetrieveSerializer(invest_queryset, many=True)
        return Response({
            'publish_results': publish_serializer.data,
            'invest_results': invest_serializer.data
        }, status=status.HTTP_200_OK)


'''


class PublishInvestSearchView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            query = request.GET.get('query', '')
            if not query:
                return Response({'error': 'Query parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
            # Split the query into individual keywords
            keywords = query.split()
            # Build Q objects for matching multiple fields
            def build_query(keywords, fields):
                query = Q()
                for keyword in keywords:
                    for field in fields:
                        query |= Q(**{f"{field}__icontains": keyword})
                return query
            # Fields to search in Publish
            publish_fields = ['title', 'author', 'organization', 'short_description', 'target_audience']
            publish_query = build_query(keywords, publish_fields)
            # Fetch and annotate Publish results
            publish_queryset = Publish.objects.filter(publish_query).annotate(
                match_score=Sum(
                    Case(
                        *[
                            When(Q(**{f"{field}__icontains": keyword}), then=1)
                            for keyword in keywords
                            for field in publish_fields
                        ],
                        output_field=IntegerField()
                    )
                )
            ).order_by('-match_score')
            publish_serializer = PublishRetrieveSerializer(publish_queryset, many=True, context={'request': request})
            # Fields to search in Invest
            invest_fields = ['title', 'description', 'category']
            invest_query = build_query(keywords, invest_fields)
            # Fetch and annotate Invest results
            invest_queryset = Invest.objects.filter(invest_query).annotate(
                match_score=Sum(
                    Case(
                        *[
                            When(Q(**{f"{field}__icontains": keyword}), then=1)
                            for keyword in keywords
                            for field in invest_fields
                        ],
                        output_field=IntegerField()
                    )
                )
            ).order_by('-match_score')

            invest_serializer = InvestRetrieveSerializer(invest_queryset, many=True, context={'request': request})

            return Response({
                'publish_results': publish_serializer.data,
                'invest_results': invest_serializer.data
            }, status=status.HTTP_200_OK)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

class RateInvestView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, id, pk):
        try:
            data = request.data
            try:
                user = CustomUser.objects.get(id=id)
            except CustomUser.DoesNotExist:
                return Response({'error': "User not found"}, status=status.HTTP_404_NOT_FOUND)
            try:
                invest = Invest.objects.get(pk=pk)
            except invest.DoesNotExist:
                return Response({"error": "Invest not found"}, status=status.HTTP_404_NOT_FOUND)
            # Check if the user has already rated the publish
            existing_rate = RateInvest.objects.filter(user=user, parent=invest).first()
            # If a rating exists, delete it to replace with the new one
            if existing_rate:
                existing_rate.delete()
                message = "Previous rating deleted and updated with new rating"
            else:
                message = "Rating successfully created"
        # Create a new rating
            RateInvest.objects.create(
                user=user,
                parent=invest,
                rate=True,
                no_of_rating=data.get('no_of_rating', 0)  # Default to 0 if no value is provided
            )
            # Calculate the total like count for the publish
            like_count = RateInvest.objects.filter(parent=invest).count()
            return Response({
                "message": message,
                "rating_count": like_count  # Return the updated like count
            }, status=status.HTTP_201_CREATED)

        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

class CommentInvestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id, pk):
        data = request.data
        print('incoming', data)

        # Try to get the user from the request
        try:
            user = CustomUser.objects.get(id=id)
        except CustomUser.DoesNotExist:
            return Response({'error': "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Try to get the Invest object
        try:
            invest = Invest.objects.get(pk=pk)
        except Invest.DoesNotExist:
            return Response({"error": "Invest not found"}, status=status.HTTP_404_NOT_FOUND)
        # Handle photo upload
        photo = request.FILES.get('photo', None)  # Get the photo file if provided

        try:
            # Create a new comment
            comment = CommentInvest.objects.create(
                user=user,
                parent=invest,
                comment=data.get('comment', ''),  # Default to an empty string if no value is provided
                photos=photo if photo else None,  # Attach photo if provided
            )

            return Response({
                "message": "Comment successfully created",
                "comment_id": comment._id,  # Assuming `id` is the primary key field
                "comment": comment.comment,
                "photo_url": comment.photos.url if comment.photos else None,  # Include the photo URL if available
            }, status=status.HTTP_201_CREATED)

        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

from .serializers import DeleteUserSerializer

class DeleteAccount(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        try:
            # Get the logged-in user
            user = request.user
            # Use the serializer to validate the phone number from the request
            serializer = DeleteUserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            # Check if the provided phone number matches the logged-in user's phone number
            phone = serializer.validated_data['phone']
            if user.phone != phone:
                raise ValidationError("The phone number does not match the logged-in user.")
            # Proceed with account deletion
            user.delete()
            return Response({"message": "Account deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except AuthenticationFailed as auth_error:
            # Handle expired or invalid token
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired. Please refresh your token."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except ValidationError as e:
            # If validation fails, print the error details
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
'''           
# View for listing and creating Invest objects
class InvestListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Invest.objects.all()
    serializer_class = InvestSerializer
'''
class InvestListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Invest.objects.all()
    serializer_class = InvestSerializer
    def get(self, request, *args, **kwargs):
        try:
            # Ensure the user is authenticated
            if not request.user.is_authenticated:
                raise AuthenticationFailed("Authentication required.")
            return super().get(request, *args, **kwargs)
        except AuthenticationFailed as auth_error:
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired or invalid. Please log in again."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        except ValidationError as e:
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            # Ensure the user is authenticated
            if not request.user.is_authenticated:
                raise AuthenticationFailed("Authentication required.")
            return super().post(request, *args, **kwargs)
        except AuthenticationFailed as auth_error:
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired or invalid. Please log in again."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        except ValidationError as e:
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

# View for retrieving, updating, and deleting an Invest object by ID
class InvestDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Invest.objects.all()  # Correct model: Invest
    serializer_class = InvestSerializer
    lookup_field = '_id'  # Ensure lookup by '_id'
    def get(self, request, *args, **kwargs):
        try:
            # Ensure the user is authenticated
            if not request.user.is_authenticated:
                raise AuthenticationFailed("Authentication required.")
            return super().get(request, *args, **kwargs)
        except AuthenticationFailed as auth_error:
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired or invalid. Please log in again."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        except ValidationError as e:
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            # Ensure the user is authenticated
            if not request.user.is_authenticated:
                raise AuthenticationFailed("Authentication required.")
            return super().post(request, *args, **kwargs)
        except AuthenticationFailed as auth_error:
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired or invalid. Please log in again."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        except ValidationError as e:
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
    # View for retrieving, updating, and deleting an Invest object by ID\
    def put(self, request, *args, **kwargs):
        try:
            # Ensure the user is authenticated
            if not request.user.is_authenticated:
                raise AuthenticationFailed("Authentication required.")

            # Print incoming data for debugging
            print("Incoming data:", request.data)

            partial = kwargs.pop('partial', False)  # Support partial updates
            instance = self.get_object()  # Retrieve the instance
            serializer = self.get_serializer(instance, data=request.data, partial=partial)

            if serializer.is_valid():
                serializer.save()  # Save updates
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # Print validation errors for debugging
                print("Validation errors:", serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except AuthenticationFailed as auth_error:
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired or invalid. Please log in again."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        except Invest.DoesNotExist:
            return Response({"error": "Invest not found."}, status=status.HTTP_404_NOT_FOUND)

                    

# View for listing and creating Publish objects
class SettingsListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
    def get(self, request, *args, **kwargs):
        try:
            # Ensure the user is authenticated
            if not request.user.is_authenticated:
                raise AuthenticationFailed("Authentication required.")
            return super().get(request, *args, **kwargs)
        except AuthenticationFailed as auth_error:
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired or invalid. Please log in again."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        except ValidationError as e:
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            # Ensure the user is authenticated
            if not request.user.is_authenticated:
                raise AuthenticationFailed("Authentication required.")
            return super().post(request, *args, **kwargs)
        except AuthenticationFailed as auth_error:
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired or invalid. Please log in again."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        except ValidationError as e:
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
# View for retrieving, updating, and deleting an Invest object by ID

# View for retrieving, updating, and deleting a Publish object
class SettingsDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
    def get(self, request, *args, **kwargs):
        try:
            # Ensure the user is authenticated
            if not request.user.is_authenticated:
                raise AuthenticationFailed("Authentication required.")
            return super().get(request, *args, **kwargs)
        except AuthenticationFailed as auth_error:
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired or invalid. Please log in again."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        except ValidationError as e:
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            # Ensure the user is authenticated
            if not request.user.is_authenticated:
                raise AuthenticationFailed("Authentication required.")
            return super().post(request, *args, **kwargs)
        except AuthenticationFailed as auth_error:
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired or invalid. Please log in again."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        except ValidationError as e:
            print("Validation error:", e.detail)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

'''

class UserFeedView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # Change as needed
    def get(self, request, user_id, *args, **kwargs):
        user = get_object_or_404(CustomUser, id=user_id)
        profile = get_object_or_404(Profile, parent=user)

        if profile.make_profile_public:
            # If the profile is public, display all Publish and Invest content
            publishes = Publish.objects.all()
            invests = Invest.objects.all()
        else:
            # If the profile is not public, show only content visible to followers
            follower_ids = profile.followers.values_list('parent__id', flat=True)
            publishes = Publish.objects.filter(parent__id__in=follower_ids)
            invests = Invest.objects.filter(parent__id__in=follower_ids)
        data = {
            'publish': PublishRetrieveSerializer(publishes, many=True, context={'request': request}).data,
            'invest': InvestRetrieveSerializer(invests, many=True, context={'request': request}).data,
        }
        return Response(data)

    def put(self, request, user_id, *args, **kwargs):
        user = get_object_or_404(CustomUser, id=user_id)
        publish_id = request.data.get('publish_id')
        invest_id = request.data.get('invest_id')

        # Update Publish
        if publish_id:
            publish = get_object_or_404(Publish, id=publish_id, parent=user)
            publish_serializer = PublishSerializer(publish, data=request.data, partial=True)
            if publish_serializer.is_valid():
                publish_serializer.save()
                return Response(publish_serializer.data, status=status.HTTP_200_OK)
            return Response(publish_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Update Invest
        if invest_id:
            invest = get_object_or_404(Invest, id=invest_id, parent=user)
            invest_serializer = InvestSerializer(invest, data=request.data, partial=True)
            if invest_serializer.is_valid():
                invest_serializer.save()
                return Response(invest_serializer.data, status=status.HTTP_200_OK)
            return Response(invest_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, user_id, *args, **kwargs):
        user = get_object_or_404(CustomUser, id=user_id)
        publish_id = request.data.get('publish_id')
        invest_id = request.data.get('invest_id')
        # Delete Publish
        if publish_id:
            publish = get_object_or_404(Publish, id=publish_id, parent=user)
            publish.delete()
            return Response({"detail": "Publish deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        # Delete Invest
        if invest_id:
            invest = get_object_or_404(Invest, id=invest_id, parent=user)
            invest.delete()
            return Response({"detail": "Invest deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

'''

class UserFeedView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # Ensure authenticated users only

    def get(self, request, user_id, *args, **kwargs):
        try:
            # Ensure the user is authenticated
            if not request.user.is_authenticated:
                raise AuthenticationFailed("Authentication required.")
            
            # Retrieve user and profile
            user = get_object_or_404(CustomUser, id=user_id)
            profile = get_object_or_404(Profile, parent=user)

            if profile.make_profile_public:
                # If the profile is public, display all Publish and Invest content
                publishes = Publish.objects.all()
                invests = Invest.objects.all()
            else:
                # If the profile is not public, show only content visible to followers
                follower_ids = profile.followers.values_list('parent__id', flat=True)
                publishes = Publish.objects.filter(parent__id__in=follower_ids)
                invests = Invest.objects.filter(parent__id__in=follower_ids)
            
            # Serialize and return the data
            data = {
                'publish': PublishRetrieveSerializer(publishes, many=True, context={'request': request}).data,
                'invest': InvestRetrieveSerializer(invests, many=True, context={'request': request}).data,
            }
            return Response(data)

        except AuthenticationFailed as auth_error:
            # Handle authentication errors
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired or invalid. Please log in again."},
                status=status.HTTP_401_UNAUTHORIZED
            )
    def put(self, request, user_id, *args, **kwargs):
        try:
            user = get_object_or_404(CustomUser, id=user_id)
            publish_id = request.data.get('publish_id')
            invest_id = request.data.get('invest_id')
            # Update Publish
            if publish_id:
                publish = get_object_or_404(Publish, id=publish_id, parent=user)
                publish_serializer = PublishSerializer(publish, data=request.data, partial=True)
                if publish_serializer.is_valid():
                    publish_serializer.save()
                    return Response(publish_serializer.data, status=status.HTTP_200_OK)
                return Response(publish_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # Update Invest
            if invest_id:
                invest = get_object_or_404(Invest, id=invest_id, parent=user)
                invest_serializer = InvestSerializer(invest, data=request.data, partial=True)
                if invest_serializer.is_valid():
                    invest_serializer.save()
                    return Response(invest_serializer.data, status=status.HTTP_200_OK)
                return Response(invest_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"detail": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
        except AuthenticationFailed as auth_error:
            # Handle authentication errors
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired or invalid. Please log in again."},
                status=status.HTTP_401_UNAUTHORIZED
            )
    def delete(self, request, user_id, *args, **kwargs):
        try:
            user = get_object_or_404(CustomUser, id=user_id)
            publish_id = request.data.get('publish_id')
            invest_id = request.data.get('invest_id')
            # Delete Publish
            if publish_id:
                publish = get_object_or_404(Publish, id=publish_id, parent=user)
                publish.delete()
                return Response({"detail": "Publish deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
            # Delete Invest
            if invest_id:
                invest = get_object_or_404(Invest, id=invest_id, parent=user)
                invest.delete()
                return Response({"detail": "Invest deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
            return Response({"detail": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

        except AuthenticationFailed as auth_error:
            # Handle authentication errors
            print("Authentication error:", auth_error)
            return Response(
                {"detail": "Token expired or invalid. Please log in again."},
                status=status.HTTP_401_UNAUTHORIZED
            )

class EnableNotificationsView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, *args, **kwargs):
        try:
            # Retrieve the profile object by user_id
            settings = Profile.objects.get(user_id=pk)
            # Update the enable_notifications field
            settings.enable_notifications = True
            settings.save()
            # Return a success response
            return Response({'enable_notifications': settings.enable_notifications}, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            # Handle the case where the Profile does not exist
            return Response({'error': 'Profile not found for the given user_id'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Handle any other exceptions
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MakeProfilePublicView(APIView):
    permission_classes = [AllowAny]

    def put(self, request, pk, *args, **kwargs):
        try:
            # Retrieve the profile object by user_id
            settings = Profile.objects.get(user_id=pk)
            # Update the make_profile_public field
            settings.make_profile_public = True
            settings.save()
            # Return a success response
            return Response({'make_profile_public': settings.make_profile_public}, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            # Handle the case where the Profile does not exist
            return Response({'error': 'Profile not found for the given user_id'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Handle any other exceptions
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ShowOnlineStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, *args, **kwargs):
        try:
            # Retrieve the profile object by user_id
            settings = Profile.objects.get(user_id=pk)
            # Update the show_online_status field
            settings.show_online_status = True
            settings.save()
            # Return a success response
            return Response({'show_online_status': settings.show_online_status}, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            # Handle the case where the Profile does not exist
            return Response({'error': 'Profile not found for the given user_id'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Handle any other exceptions
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EnableTwoFactorAuthenticationView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, *args, **kwargs):
        try:
            # Retrieve the profile object by user_id
            settings = Profile.objects.get(user_id=pk)
            # Update the two_factor_authentication field
            settings.two_factor_authentication = True
            settings.save()
            # Return a success response
            return Response({'two_factor_authentication': settings.two_factor_authentication}, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            # Handle the case where the Profile does not exist
            return Response({'error': 'Profile not found for the given user_id'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Handle any other exceptions
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
>>>>>>> 2b11a5b (first commit)
