export default [
  {
    _name: 'CSidebarNav',
    _children: [
      {
        _name: 'CSidebarNavItem',
        name: '數據總覽',
        to: '/dashboard',
        icon: 'cil-speedometer',
      },
      {
        _name: 'CSidebarNavTitle',
        _children: ['管理系統']
      },
      {
        _name: 'CSidebarNavItem',
        name: '駕駛管理',
        to: '/driver',
        icon: 'cil-people',
      },
      {
        _name: 'CSidebarNavItem',
        name: '車輛管理',
        to: '/car',
        icon: 'cil-car-alt',
      },
      {
        _name: 'CSidebarNavItem',
        name: '車牌管理',
        to: '/carPlate',
        icon: 'cil-spreadsheet',
      },
      {
        _name: 'CSidebarNavTitle',
        _children: ['數據分析']
      },
      {
        _name: 'CSidebarNavItem',
        name: '車輛追蹤',
        to: '/tracking',
        icon: 'cil-map',
      },
      {
        _name: 'CSidebarNavItem',
        name: '駕駛分析',
        to: '/driverAnalysis',
        icon: 'cil-chart-line',
      },
      {
        _name: 'CSidebarNavItem',
        name: '車輛分析',
        to: '/carAnalysis',
        icon: 'cil-chart-line',
      },
    ]
  }
]