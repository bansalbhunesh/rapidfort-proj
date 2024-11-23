# Base image for React frontend
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install --legacy-peer-deps

# Copy the rest of the application code
COPY . .

# Build the production application
RUN npm run build

# Expose the default Next.js/React port
EXPOSE 3000

# Start the application in production mode
CMD ["npm", "start"]
