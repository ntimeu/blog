#include <sys/epoll.h>

int main(void)
{
    intepfd=0,ret=0;
    structepoll_eventev;
    charc;

    epfd=epoll_create(1);
    if(epfd==-1){
        perror("epoll_wait()");
        return1;
    }

    ev.events=EPOLLIN;
    ev.data.ptr=NULL;
    ret=epoll_ctl(epfd,EPOLL_CTL_ADD,0,&ev);
    if(ret==-1){
        perror("epoll_ctl()");
        return2;
    }

    for(;;){
        ret=epoll_wait(epfd,&ev,1,-1);
        if(ret>0){
            while((c=getchar())!='\n')
                putchar(c);
            putchar('\n');
            fflush(stdin);
        }elseif(ret==0){
            break;
        }else{
            perror("epoll_wait()");
            break;
        }
    }
    close(epfd);
    return0;
}
