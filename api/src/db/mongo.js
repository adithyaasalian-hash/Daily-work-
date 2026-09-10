import mongoose from 'mongoose';
import { env } from '../config/env.js';

export async function connectMongo() {
  mongoose.set('strictQuery', true);
  await mongoose.connect(env.mongoUri, {
    dbName: env.mongoDb,
    serverSelectionTimeoutMS: 8000,
  });
  console.log(`[mongo] connected to ${env.mongoDb}`);
  return mongoose.connection;
}

export async function disconnectMongo() {
  await mongoose.disconnect();
}
