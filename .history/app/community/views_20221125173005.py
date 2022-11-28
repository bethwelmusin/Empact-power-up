from django.shortcuts import render

# Create your views here.
class GetAllPublishedBlogApiView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    @swagger_auto_schema(
        # request_body=GetPostSerializer,
        responses={
            '200': GetPostSerializer,
            '400': ErrorSerializer,

        },
        operation_description=' An api endpoint to get all published blogs. NOTE: When creating a blog post by default status is draft.'
    )
    def get(self, request):
        posts = Post.objects.filter(status='published').all()
        serializer = GetPostSerializer(posts, many=True)
        return Response({
            'status': True,
            'message': 'Blog data fetched successfull',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data,
        })

