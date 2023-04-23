import functions as fun
import strings as ss
# club == public == event

customid = str(input())
if(ss.src_vk in customid):
    re_custom_id = customid.split('/')[-1]
    data = fun.vk_get_screen_name(custom_url=re_custom_id)
    print(data)



