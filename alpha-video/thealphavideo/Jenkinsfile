node {    
      def app     
      stage('Clone repository') {               
             
            checkout scm    
      }     
      stage('Build image') {         
       
            sh 'docker buildx use multibuilder && docker buildx build  --push  --platform linux/arm/v7,linux/arm64/v8,linux/amd64  --tag andrewstech/alpha-video:latest .'
       }     
      
     
}
