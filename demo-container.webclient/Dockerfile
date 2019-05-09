FROM node:10.15.3
RUN mkdir /usr/src/app/
WORKDIR /usr/src/app/
ENV PATH=/usr/src/app/node_modules/.bin:$PATH
COPY . /usr/src/app
COPY package.json /usr/src/app/package.json
EXPOSE 3000
RUN npm install --silent
RUN npm install react-scripts@3.0.0 -g --silent

CMD [ "npm", "start" ]