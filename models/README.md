# AI Models Directory

This directory contains trained AI models, evaluation tools, and deployment utilities for the Furniture Recommendation Platform.

## 📁 Directory Structure

```
models/
├── README.md                    # This file
├── ModelTraining.ipynb          # Complete model training notebook
├── model_evaluation.py          # Model evaluation utilities
├── deploy_integration.py        # Deployment integration script
├── test_queries.txt            # Test queries for evaluation
└── [Generated after training]
    ├── model_config.json        # Model configuration
    ├── product_embeddings.npy   # Pre-trained embeddings
    ├── vector_db.pkl            # Vector database
    └── product_metadata.pkl     # Product metadata
```

## 🚀 Getting Started

### 1. Model Training

Run the training notebook to generate AI models:

```bash
# Open Jupyter notebook
jupyter notebook ModelTraining.ipynb

# Or run with specific Python environment
python -m jupyter notebook ModelTraining.ipynb
```

**The notebook will:**
- Load and preprocess the furniture dataset
- Train text embeddings using SentenceTransformer
- Set up computer vision models for image processing
- Generate AI descriptions with FLAN-T5
- Create vector database for semantic search
- Evaluate model performance with comprehensive metrics
- Export model artifacts for deployment

### 2. Model Evaluation

Use the evaluation utilities for benchmarking:

```python
from model_evaluation import ModelEvaluator, quick_evaluate

# Quick evaluation
metrics = quick_evaluate(embedding_model, vector_db, test_queries)
print(f"Precision@5: {metrics['precision_at_5']:.3f}")

# Comprehensive evaluation
evaluator = ModelEvaluator(embedding_model, vector_db)
full_metrics = evaluator.benchmark_search_performance(test_queries)
report = evaluator.generate_evaluation_report(full_metrics)
```

### 3. Deployment Integration

Deploy trained models to your backend:

```python
from deploy_integration import ModelDeploymentManager

# Initialize deployment manager
deploy_manager = ModelDeploymentManager()

# Run deployment checklist
checklist = deploy_manager.run_deployment_checklist()

# Generate integration code
if all(checklist.values()):
    integration_code = deploy_manager.generate_backend_integration_code()
    
    # Copy artifacts to backend
    deploy_manager.copy_model_artifacts_to_backend("../backend/models/")
```

## 📊 Model Performance Metrics

The training process tracks several key metrics:

### Search Quality
- **Precision@K**: Relevance of top-K search results
- **Recall@K**: Coverage of relevant items in top-K results  
- **MRR (Mean Reciprocal Rank)**: Quality of ranking

### Performance
- **Search Latency**: Time to process queries and return results
- **Embedding Quality**: Semantic similarity accuracy
- **Model Size**: Memory and storage requirements

### Expected Performance Targets
- Precision@5: > 60%
- Average Search Time: < 100ms
- MRR: > 0.5
- Model Loading Time: < 30s

## 🧪 Testing & Validation

### Test Queries
The `test_queries.txt` file contains 50 curated furniture search queries covering:
- Office furniture
- Living room items  
- Bedroom furniture
- Storage solutions
- Dining room pieces
- Outdoor furniture

### Evaluation Framework
- **A/B Testing**: Compare different model configurations
- **Cross-validation**: Ensure consistent performance
- **Human evaluation**: Quality assessment by furniture experts
- **Performance benchmarking**: Speed and accuracy metrics

## 🛠️ Model Configurations

### Text Embeddings
- **Model**: `sentence-transformers/all-MiniLM-L6-v2`
- **Dimensions**: 384
- **Context Length**: 512 tokens
- **Language**: English (furniture domain)

### Computer Vision  
- **Model**: ResNet-50 (pre-trained)
- **Input Size**: 224x224 pixels
- **Features**: 2048 dimensions
- **Use Case**: Image similarity search

### Generative AI
- **Model**: `google/flan-t5-small`  
- **Max Length**: 80 tokens
- **Temperature**: 0.7
- **Use Case**: Product descriptions

## 📈 Monitoring & Maintenance

### Model Retraining Schedule
- **Weekly**: Update with new product data
- **Monthly**: Full model retraining
- **Quarterly**: Architecture evaluation
- **Annually**: Major model upgrades

### Performance Monitoring
```python
# Monitor search performance
evaluator = ModelEvaluator(embedding_model, vector_db)
daily_metrics = evaluator.benchmark_search_performance(production_queries)

# Alert thresholds
if daily_metrics.precision_at_k[5] < 0.5:
    send_alert("Model performance degraded")
```

## 🔧 Troubleshooting

### Common Issues

#### 1. Model Loading Errors
```bash
# Check dependencies
pip install -r requirements.txt

# Verify model artifacts exist
python -c "from deploy_integration import ModelDeploymentManager; ModelDeploymentManager().validate_model_artifacts()"
```

#### 2. Low Search Quality
- Check embedding model performance
- Validate training data quality
- Retrain with more diverse examples
- Adjust similarity thresholds

#### 3. Slow Performance
- Use approximate similarity search (Faiss)
- Implement model quantization
- Cache frequent queries
- Optimize vector operations

#### 4. Memory Issues
- Reduce batch sizes during training
- Use model checkpointing
- Implement lazy loading
- Consider model distillation

## 💡 Best Practices

### Model Development
1. **Version Control**: Track model versions and configurations
2. **Reproducibility**: Set random seeds and log training parameters
3. **Validation**: Always validate on held-out test sets
4. **Documentation**: Document model architecture and decisions

### Production Deployment
1. **Gradual Rollout**: Deploy to subset of users first
2. **Monitoring**: Track key performance metrics
3. **Rollback Plan**: Keep previous model version ready
4. **A/B Testing**: Compare model performance in production

### Data Management
1. **Quality Control**: Clean and validate training data
2. **Privacy**: Ensure compliance with data protection regulations
3. **Bias Detection**: Monitor for algorithmic bias
4. **Continuous Updates**: Regularly refresh training data

## 📚 Additional Resources

- [SentenceTransformers Documentation](https://www.sbert.net/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/)
- [Scikit-learn Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [FastAPI Production Deployment](https://fastapi.tiangolo.com/deployment/)

## 🆘 Support

For model training issues or deployment questions:

1. Check the troubleshooting section above
2. Review training logs and evaluation metrics
3. Validate data quality and preprocessing steps
4. Test with smaller datasets first
5. Check hardware requirements (CPU/GPU/Memory)

## 🎯 Next Steps

After completing model training:

1. ✅ Run the ModelTraining.ipynb notebook
2. ✅ Evaluate model performance with test queries  
3. ✅ Generate deployment integration code
4. ✅ Copy model artifacts to backend directory
5. ✅ Update FastAPI backend with trained models
6. ✅ Test end-to-end search functionality
7. ✅ Monitor production performance metrics

The AI-powered furniture recommendation system is now ready for production deployment! 🚀