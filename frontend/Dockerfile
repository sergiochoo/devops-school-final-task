FROM node:14.18.1-stretch as build

WORKDIR /usr/app

COPY package.json package-lock.json ./
RUN npm i

COPY . .
RUN npm run build


FROM nginx:1.20.2-alpine

COPY --from=build /usr/app/build /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]