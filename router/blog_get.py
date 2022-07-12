from router.blog_post import required_functionality
from fastapi import APIRouter, Response, status, Depends
from enum import Enum
from typing import Optional


router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

# @app.get('/blog/all')
# def get_all_blogs():
#     return {'message': 'All blogs provided'}

@router.get(
    '/all',
    summary='Retreeve all blogs',
    description='This api call simulated fetching all blogs.',
    response_description='The list of available blogs'
    )
def get_blogs(page = 1, page_size: Optional[int] = None, req_parameter: dict = Depends(required_functionality)):
    return {'message': f'All {page_size} blogs on page {page}', 'req': req_parameter}

@router.get('/{id}/comments/{comment_id}', tags=['comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None, req_parameter: dict = Depends(required_functionality)):
    """
    Simulated retrieving a comment of a blog

    - **id** mandatory path parametr
    - **comment_id** mandatory path parametr
    - **valid** optional query parametr
    - **username** optional query parametr
    """
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get('/type/{type}')
def get_blog_type(type: BlogType, req_parameter: dict = Depends(required_functionality)):
    return {'message': f'Blogs type {type}'}

@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id}'}

