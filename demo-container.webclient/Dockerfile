FROM node:10.15.3
# RUN mkdir /usr/src/app/

WORKDIR /usr/src/app/
ENV PATH=/usr/src/app/node_modules/.bin:$PATH
COPY package.json /usr/src/app/package.json

RUN npm install --silent
RUN npm install react-scripts@3.0.0 -g --silent

COPY . /usr/src/app
RUN npm run build

FROM nginx:1.15.12-alpine
RUN rm -rf /etc/nginx/conf.d
COPY conf /etc/nginx

COPY --from=builder /usr/src/app/build /usr/share/nginx/html

EXPOSE 80

# CMD [ "npm", "start" ]
CMD [ "nginx", "-g", "daemon off;" ]