# Project: 0x0F. Load balancer

### Background Context
Given 2 additional servers:

gc-[STUDENT_ID]-web-02-XXXXXXXXXX
gc-[STUDENT_ID]-lb-01-XXXXXXXXXX
Improved the web stack so that there is redundancy for my web servers. This will allow me to be able to accept more traffic by doubling the number of web servers, and to make the infrastructure more reliable. If one web server fails, I will still have a second one to handle requests.

For this project, I wrote Bash scripts to automate my work. All scripts are designed to configure a brand new Ubuntu server to match the task requirements.

## Resources

#### Resources:

* [Introduction to load-balancing and HAproxy](https://intranet.alxswe.com/rltoken/B7f3oz8i3Xvvom_YQZzLnQ)
* [HTTP header](https://intranet.alxswe.com/rltoken/sZ9v3Vq2tgLwN_PWVQketw)
* [Debian/Ubuntu HAProxy packages](https://intranet.alxswe.com/rltoken/2VRAgtKKR9g6Xfb0xzGiSg)
## Tasks

| Task | File |
| ---- | ---- |
| 0. Double the number of webservers | [0-custom_http_response_header](./0-custom_http_response_header) |
| 1. Install your load balancer | [1-install_load_balancer](./1-install_load_balancer) |
