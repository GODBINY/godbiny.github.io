import os
import re
from urllib.parse import quote

# List of all blog post file paths
file_paths = [
    '/Users/godbin/workspace/godbiny.github.io/data/blog/wikiData/Wiki-関数.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2025/08/session-test.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2025/08/BackTracking.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/12/[함수형프로그래밍]함수형 프로그래밍 개념.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/12/[프로그래머스][JavaScript]콜라츠 수열 만들기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/12/[프로그래머스][JavaScript]카운트 업.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/12/[프로그래머스][JavaScript]주사위 게임 2.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/12/[프로그래머스][JavaScript]이어 붙인 수.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/12/[프로그래머스][JavaScript]원소들의 곱과합.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/12/[프로그래머스][JavaScript]수열과 구간 쿼리 4.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/12/[프로그래머스][JavaScript]수열과 구간 쿼리 3.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/12/[프로그래머스][JavaScript]수열과 구간 쿼리 2.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/12/[프로그래머스][JavaScript]수 조작하기2.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/12/[프로그래머스][JavaScript]수 조작하기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/12/[프로그래머스][JavaScript]배열 비교하기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/12/[프로그래머스][JavaScript]마지막 두 원소.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/12/[프로그래머스][JavaScript]뒤에서 5등까지.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/12/[성능개선]코드 분할.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/11/[프로그래머스][JavaScript]코드 처리하기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/11/[프로그래머스][JavaScript]등차수열의 특정한 항만 더하기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/11/[프로그래머스][JavaScript]flag에 따라 다른 값 반환하기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/10/개발자 도구 Media tab 에서 의미하는 것들.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/10/[프로그래머스][JavaScript]홀짝에 따라 다른 값 반환하기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/10/[프로그래머스][JavaScript]홀짝 구분하기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/10/[프로그래머스][JavaScript]특수문자 출력하기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/10/[프로그래머스][JavaScript]조건 문자열.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/10/[프로그래머스][JavaScript]문자열 출력하기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/10/[프로그래머스][JavaScript]문자열 섞기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/10/[프로그래머스][JavaScript]문자열 붙여서 출력하기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/10/[프로그래머스][JavaScript]문자열 반복해서 출력하기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/10/[프로그래머스][JavaScript]문자열 돌리기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/10/[프로그래머스][JavaScript]문자열 곱하기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/10/[프로그래머스][JavaScript]문자열 겹쳐쓰기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/10/[프로그래머스][JavaScript]문자리스트를 문자열로 변환하기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/10/[프로그래머스][JavaScript]두 수의 연산값 비교하기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/10/[프로그래머스][JavaScript]덧셈식 출력하기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/10/[프로그래머스][JavaScript]더 크게 합치기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/10/[프로그래머스][JavaScript]대소문자 바꿔서 출력하기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/10/[프로그래머스][JavaScript]공배수.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/10/[프로그래머스][JavaScript]n의 배수.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/10/[프로그래머스][JavaScript]a와 b 출력하기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2025/08/lazyvim-테마-변경하기.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2025/08/session&JWT.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2025/07/git commands.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2025/07/SEO.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/09/AWS CloudFront cache polices.mdx',
    '/Users/godbin/workspace/godbiny.github.io/data/blog/2024/12/[프로그래머스][JavaScript]rny_string.mdx'
]

def generate_slug(file_path):
    base_path = '/Users/godbin/workspace/godbiny.github.io/data/blog/'
    relative_path = file_path.replace(base_path, '')
    
    # Remove extension
    path_without_ext = relative_path.rsplit('.', 1)[0]
    
    # Replace spaces with hyphens
    slug_temp = re.sub(r'\s+', '-', path_without_ext)
    
    # URL-encode the entire slug, keeping / and - unencoded
    final_slug = quote(slug_temp, safe='/-()') # Removed [] from safe characters, added () for safety
    
    return final_slug

for file_path in file_paths:
    with open(file_path, 'r+') as f:
        content = f.read()
        
        # Check if slug is already present and correctly formatted (URL-encoded)
        # This check is more robust now.
        frontmatter_match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
        if frontmatter_match:
            frontmatter_content = frontmatter_match.group(1)
            if 'slug:' in frontmatter_content:
                # If slug is present, check if it's already URL-encoded
                existing_slug_match = re.search(r"slug:\s*(.*)", frontmatter_content) # Simplified regex
                if existing_slug_match:
                    existing_slug = existing_slug_match.group(1).strip().strip("'\"") # Remove quotes if present
                    # If it looks like a URL-encoded slug, skip
                    if '%' in existing_slug or re.search(r'[^\w\s\-\/.]', existing_slug):
                        continue # Skip if already URL-encoded or contains problematic chars
        
        slug = generate_slug(file_path)
        
        lines = content.splitlines()
        
        # Find the position to insert the slug (after title or date, or summary)
        insert_index = -1
        for i, line in enumerate(lines):
            if line.strip().startswith('summary:'):
                insert_index = i + 1
                break
            elif line.strip().startswith('date:'):
                insert_index = i + 1
            elif line.strip().startswith('title:'):
                insert_index = i + 1
        
        if insert_index != -1:
            lines.insert(insert_index, f'slug: \'{slug}\'')
        else: # Fallback if no suitable line found, insert after first '---'
            lines.insert(1, f'slug: \'{slug}\'')
            
        new_content = '\n'.join(lines)
        
        f.seek(0)
        f.write(new_content)
        f.truncate()

print('Done.')
