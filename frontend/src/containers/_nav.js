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
        icon: 'cil-drop',
      },
      {
        _name: 'CSidebarNavItem',
        name: '車輛管理',
        to: '/car',
        icon: 'cil-pencil',
      },
      {
        _name: 'CSidebarNavTitle',
        _children: ['數據分析']
      },
      {
        _name: 'CSidebarNavDropdown',
        name: '數據統計',
        route: '/data',
        icon: 'cil-puzzle',
        items: [
          {
            name: '車輛追蹤',
            to: '/data/tracking'
          },
          {
            name: '駕駛分析',
            to: '/data/driverAnalysis'
          },
          {
            name: '車輛分析',
            to: '/data/carAnalysis'
          }, 
        ]
      },
    ]
  }
]