# [Problem](https://projecteuler.net/problem=3) No. 3
## Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number **600851475143** ?


[![](https://mermaid.ink/img/eyJjb2RlIjoic3RhdGVEaWFncmFtLXYyXG4gICAgWypdIC0tPiA2MDA4NTE0NzUxNDNcbiAgICA2MDA4NTE0NzUxNDMgLS0-IGxvbmdfblxuICAgIGxvbmdfbiAtLT4gTnVtYmVyQ2hlY2tfKDw9MSlcbiAgICBOdW1iZXJDaGVja18oPD0xKSAtLT4gSXNfZ2l2ZW5Db25kaXRpb25fdHJ1ZT9cbiAgICBJc19naXZlbkNvbmRpdGlvbl90cnVlPyAtLT4gWWVzXG4gICAgSXNfZ2l2ZW5Db25kaXRpb25fdHJ1ZT8gLS0-IE5vXG4gICAgWWVzIC0tPiBpbnRfZGl2XG4gICAgaW50X2RpdiAtLT4gd2hpbGUoZGl2XzxfbnVtYmVyKVxuICAgIHdoaWxlKGRpdl88X251bWJlcikgLS0-IFllcy5cbiAgICB3aGlsZShkaXZfPF9udW1iZXIpIC0tPiBOby5cbiAgICBZZXMuIC0tPiBpZijwnZmjX2lzX_Cdl7vwnZe88J2YgV9hX2ZhY3Rvcl9vZl_wnZmZ8J2ZnvCdmaspXz9cbiAgICBMYXJnZXN0X1ByaW1lX0ZhY3Rvcl9pc1_wnZ-sIC0tPiBbKl1cbiAgICBQcmludF9MYXJnZXN0X1ByaW1lRmFjdG9yIC0tPiBbKl1cbiAgICBpZijwnZmjX2lzX_Cdl7vwnZe88J2YgV9hX2ZhY3Rvcl9vZl_wnZmZ8J2ZnvCdmaspXz8gLS0-IFRydWVcbiAgICBpZijwnZmjX2lzX_Cdl7vwnZe88J2YgV9hX2ZhY3Rvcl9vZl_wnZmZ8J2ZnvCdmaspXz8gLS0-IEZhbHNlXG4gICAgVHJ1ZSAtLT4gZGl2KytcbiAgICBkaXYrKyAtLT4gd2hpbGUoZGl2XzxfbnVtYmVyKVxuICAgIEZhbHNlIC0tPiBuL2RpdlxuICAgIEZhbHNlIC0tPiBkaXY9MlxuICAgIG4vZGl2IC0tPiB3aGlsZShkaXZfPF9udW1iZXIpXG4gICAgZGl2PTIgLS0-IHdoaWxlKGRpdl88X251bWJlcilcbiAgICBOby4gLS0-IFByaW50X0xhcmdlc3RfUHJpbWVGYWN0b3JcbiAgICBObyAtLT4gTGFyZ2VzdF9QcmltZV9GYWN0b3JfaXNf8J2frCIsIm1lcm1haWQiOnt9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic3RhdGVEaWFncmFtLXYyXG4gICAgWypdIC0tPiA2MDA4NTE0NzUxNDNcbiAgICA2MDA4NTE0NzUxNDMgLS0-IGxvbmdfblxuICAgIGxvbmdfbiAtLT4gTnVtYmVyQ2hlY2tfKDw9MSlcbiAgICBOdW1iZXJDaGVja18oPD0xKSAtLT4gSXNfZ2l2ZW5Db25kaXRpb25fdHJ1ZT9cbiAgICBJc19naXZlbkNvbmRpdGlvbl90cnVlPyAtLT4gWWVzXG4gICAgSXNfZ2l2ZW5Db25kaXRpb25fdHJ1ZT8gLS0-IE5vXG4gICAgWWVzIC0tPiBpbnRfZGl2XG4gICAgaW50X2RpdiAtLT4gd2hpbGUoZGl2XzxfbnVtYmVyKVxuICAgIHdoaWxlKGRpdl88X251bWJlcikgLS0-IFllcy5cbiAgICB3aGlsZShkaXZfPF9udW1iZXIpIC0tPiBOby5cbiAgICBZZXMuIC0tPiBpZijwnZmjX2lzX_Cdl7vwnZe88J2YgV9hX2ZhY3Rvcl9vZl_wnZmZ8J2ZnvCdmaspXz9cbiAgICBMYXJnZXN0X1ByaW1lX0ZhY3Rvcl9pc1_wnZ-sIC0tPiBbKl1cbiAgICBQcmludF9MYXJnZXN0X1ByaW1lRmFjdG9yIC0tPiBbKl1cbiAgICBpZijwnZmjX2lzX_Cdl7vwnZe88J2YgV9hX2ZhY3Rvcl9vZl_wnZmZ8J2ZnvCdmaspXz8gLS0-IFRydWVcbiAgICBpZijwnZmjX2lzX_Cdl7vwnZe88J2YgV9hX2ZhY3Rvcl9vZl_wnZmZ8J2ZnvCdmaspXz8gLS0-IEZhbHNlXG4gICAgVHJ1ZSAtLT4gZGl2KytcbiAgICBkaXYrKyAtLT4gd2hpbGUoZGl2XzxfbnVtYmVyKVxuICAgIEZhbHNlIC0tPiBuL2RpdlxuICAgIEZhbHNlIC0tPiBkaXY9MlxuICAgIG4vZGl2IC0tPiB3aGlsZShkaXZfPF9udW1iZXIpXG4gICAgZGl2PTIgLS0-IHdoaWxlKGRpdl88X251bWJlcilcbiAgICBOby4gLS0-IFByaW50X0xhcmdlc3RfUHJpbWVGYWN0b3JcbiAgICBObyAtLT4gTGFyZ2VzdF9QcmltZV9GYWN0b3JfaXNf8J2frCIsIm1lcm1haWQiOnt9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)