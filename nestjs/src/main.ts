import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import cluster from 'cluster';
import { cpus } from 'os';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  const numCPUs = cpus().length;
  if (cluster.isPrimary) {
    console.log(`Primary ${process.pid} is running`);

    for (let i = 0; i < numCPUs; i++) {
      cluster.fork();
    }

    cluster.on('exit', (worker) => {
      console.log(`worker ${worker.process.pid} died`);
    });
  } else {
    await app.listen(process.env.PORT || 3000);

    console.log(`Worker ${process.pid} started`);
  }
}
bootstrap();
