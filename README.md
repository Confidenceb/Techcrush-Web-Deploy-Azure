# Techcrush Web Deploy

A professional portfolio website showcasing frontend development skills and DevOps aspirations.

## Features

- Responsive design with gradient backgrounds
- Profile section with avatar image
- Contact links to GitHub and other platforms
- Clean, modern UI using Inter font

## Technologies Used

- HTML5
- CSS3
- Google Fonts (Inter)

## Deployment to Azure Static Web Apps

This project is configured for automatic deployment to Azure Static Web Apps via GitHub Actions.

### Prerequisites

1. An Azure account
2. A GitHub repository

### Deployment Steps

1. **Create Azure Static Web App**:
   - Go to the Azure portal
   - Search for "Static Web Apps"
   - Click "Create"
   - Choose your subscription and resource group
   - Name your app (e.g., "techcrush-portfolio")
   - Select "GitHub" as the deployment source
   - Sign in to GitHub and select this repository
   - Choose the main branch
   - For build details:
     - Build preset: Custom
     - App location: `/`
     - Api location: (leave empty)
     - Output location: (leave empty)
   - Click "Review + create"

2. **Configure GitHub Secrets**:
   - After creating the Static Web App, go to the resource in Azure portal
   - Go to "Configuration" > "Environment variables"
   - Copy the "AZURE_STATIC_WEB_APPS_API_TOKEN" value
   - In your GitHub repository, go to Settings > Secrets and variables > Actions
   - Add a new repository secret named `AZURE_STATIC_WEB_APPS_API_TOKEN` with the copied value

3. **Deploy**:
   - Push this code to the main branch of your GitHub repository
   - The GitHub Actions workflow will automatically build and deploy your site
   - You can monitor the deployment in the Actions tab of your repository

4. **Access Your Site**:
   - Once deployed, you'll get a URL like `https://gentle-ocean-0d4b8b303.azurestaticapps.net`
   - You can also find the URL in the Azure portal under your Static Web App resource

## Local Development

To run locally:

1. Clone the repository
2. Open `index.html` in your browser
3. No build process required - it's pure HTML/CSS

## Data

The `data.json` file contains geographic coordinates for Lagos cities, verified for accuracy with 4 decimal precision (~11 meters accuracy). This data can be used for mapping applications or location services.

## Contributing

Feel free to submit issues and pull requests!