const axios = require('axios');

const testAPI = async () => {
  console.log('Testing frontend to backend connectivity...\n');

  // Test 1: Direct backend health check
  console.log('1. Testing direct backend connection:');
  try {
    const response = await axios.get('http://localhost:8001/health');
    console.log('✅ Backend health check:', response.data);
  } catch (error) {
    console.log('❌ Backend health check failed:', error.message);
  }

  // Test 2: Direct backend search API
  console.log('\n2. Testing direct backend search API:');
  try {
    const response = await axios.post('http://localhost:8001/api/search', {
      query: 'modern sofa',
      session_id: 'test_session',
      max_results: 3
    });
    console.log('✅ Backend search API:', response.data.success ? 'Success' : 'Failed');
    console.log('   Message:', response.data.message.substring(0, 100) + '...');
    console.log('   Results count:', response.data.results?.length || 0);
  } catch (error) {
    console.log('❌ Backend search API failed:', error.message);
  }

  // Test 3: Test CORS
  console.log('\n3. Testing CORS headers:');
  try {
    const response = await axios.get('http://localhost:8001/health', {
      headers: {
        'Origin': 'http://localhost:3000'
      }
    });
    console.log('✅ CORS test passed');
  } catch (error) {
    console.log('❌ CORS test failed:', error.message);
  }
};

testAPI();