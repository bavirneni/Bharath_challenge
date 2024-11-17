# Use the official Nginx image as the base image
FROM nginx:latest

# Copy the custom HTML file to the default Nginx location

COPY ssl-key/privkey.pem /etc/ssl/private/privkey.pem
COPY ssl-key/fullchain.pem /etc/ssl/private/fullchain.pem

COPY index.html /usr/share/nginx/html/index.html
COPY nginx.conf /etc/nginx/nginx.conf


# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]