<template>
  <div class="home-page">
    <div class="welcome-section">
      <h1 class="title">欢迎使用管理系统</h1>
      <p class="subtitle">高效、便捷的管理平台</p>
    </div>

    <div class="stats-section">
      <a-row :gutter="16">
        <a-col :span="6">
          <a-card class="stat-card">
            <div class="stat-content">
              <div class="stat-number">1,234</div>
              <div class="stat-label">用户总数</div>
            </div>
          </a-card>
        </a-col>
        <a-col :span="6">
          <a-card class="stat-card">
            <div class="stat-content">
              <div class="stat-number">567</div>
              <div class="stat-label">订单数量</div>
            </div>
          </a-card>
        </a-col>
        <a-col :span="6">
          <a-card class="stat-card">
            <div class="stat-content">
              <div class="stat-number">89</div>
              <div class="stat-label">产品数量</div>
            </div>
          </a-card>
        </a-col>
        <a-col :span="6">
          <a-card class="stat-card">
            <div class="stat-content">
              <div class="stat-number">98%</div>
              <div class="stat-label">完成率</div>
            </div>
          </a-card>
        </a-col>
      </a-row>
    </div>

    <a-row :gutter="16">
      <a-col :span="16">
        <a-card title="数据图表" class="chart-card">
          <div ref="chartContainer" class="chart-container" />
        </a-card>
      </a-col>
      <a-col :span="8">
        <a-card title="快速操作">
          <div class="quick-actions">
            <a-button type="primary" block class="action-btn">创建用户</a-button>
            <a-button block class="action-btn">添加产品</a-button>
            <a-button block class="action-btn">查看报表</a-button>
            <a-button block class="action-btn">系统设置</a-button>
          </div>
        </a-card>
        <a-card title="最新活动" style="margin-top: 16px;">
          <div class="activity-item" v-for="(activity, index) in activities" :key="index">
            <div class="activity-content">
              <div class="activity-text">{{ activity.text }}</div>
              <div class="activity-time">{{ activity.time }}</div>
            </div>
          </div>
        </a-card>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import { 
  Row, 
  Col, 
  Card, 
  Button 
} from 'ant-design-vue';
import { ref, onMounted } from 'vue';
import { Line } from '@antv/g2plot';

export default {
  name: 'NewHome',
  components: {
    ARow: Row,
    ACol: Col,
    ACard: Card,
    AButton: Button,
  },
  setup() {
    const chartContainer = ref();
    let lineChart;
    
    const activities = [
      { text: '张三创建了新用户', time: '10分钟前' },
      { text: '李四更新了系统配置', time: '25分钟前' },
      { text: '王五完成了订单处理', time: '40分钟前' },
      { text: '赵六上传了新文档', time: '1小时前' },
      { text: '钱七审核了用户申请', time: '2小时前' },
    ];

    onMounted(() => {
      const data = [
        { year: '1月', value: 380 },
        { year: '2月', value: 520 },
        { year: '3月', value: 456 },
        { year: '4月', value: 420 },
        { year: '5月', value: 680 },
        { year: '6月', value: 586 },
        { year: '7月', value: 620 },
        { year: '8月', value: 720 },
        { year: '9月', value: 680 },
        { year: '10月', value: 780 },
        { year: '11月', value: 890 },
        { year: '12月', value: 950 },
      ];

      lineChart = new Line(chartContainer.value, {
        data,
        xField: 'year',
        yField: 'value',
        point: {
          size: 5,
          shape: 'diamond',
        },
        tooltip: {
          formatter: (datum) => {
            return { name: '销售额', value: datum.value };
          },
        },
      });
      
      lineChart.render();
    });

    return {
      chartContainer,
      activities,
    };
  },
};
</script>

<style scoped>
.home-page {
  padding: 24px;
}

.welcome-section {
  text-align: center;
  margin-bottom: 24px;
}

.title {
  font-size: 28px;
  color: #1890ff;
  margin-bottom: 8px;
}

.subtitle {
  font-size: 16px;
  color: #888;
}

.stats-section {
  margin-bottom: 24px;
}

.stat-card {
  text-align: center;
}

.stat-content {
  padding: 16px 0;
}

.stat-number {
  font-size: 24px;
  font-weight: bold;
  color: #1890ff;
  margin-bottom: 8px;
}

.stat-label {
  color: #999;
  font-size: 14px;
}

.chart-card {
  height: 400px;
}

.chart-container {
  height: 320px;
}

.quick-actions {
  padding: 8px 0;
}

.action-btn {
  margin-bottom: 12px;
}

.activity-item {
  padding: 8px 0;
  border-bottom: 1px solid #f0f0f0;
}

.activity-item:last-child {
  border-bottom: none;
}

.activity-content {
  display: flex;
  justify-content: space-between;
}

.activity-text {
  color: #333;
}

.activity-time {
  color: #999;
  font-size: 12px;
}
</style>