    
class StrategySettings():
    strategy_notes = [  
    
        ("cron", {                              # Ключ - название стратегии, можно любой например с суфиксами (volf_stoch1)
            "LONG": {
                "entry_conditions": {
                    "rules": {
                        'CRON': {
                            'enable': True,            # True/False -- использовать/не использовать
                            'tfr': "5m",
                            'period': 0,
                            "ind_name": 'CRON_IND'
                        },  #               
                    },     
                    "is_close_bar": True,             # Дожидаться закрытия бара                
                    "grid_orders": [
                        {'indent': 0.0, 'volume': 14, 'signal': True},
                        {'indent': -7.0, 'volume': 14, 'signal': False}, # %
                        {'indent': -14.0, 'volume': 14, 'signal': False}, # %
                        {'indent': -21.0, 'volume': 14, 'signal': False}, # %
                        {'indent': -28.0, 'volume': 14, 'signal': False}, # %
                        {'indent': -35.0, 'volume': 14, 'signal': False}, # %
                        {'indent': -42.0, 'volume': 14, 'signal': False}, # %
                    ],                      
                },

                "exit_conditions": {                              
                    "close_by_signal": {
                        "is_active": False,    # Закрытие по сигналу
                        "min_profit": 0.6,   # Минимальный профит при закрытии по сигналу. None -- откл
                    },  
                    "trailing_sl": {
                        "enable": False,
                        "is_move_tp": True,
                        "val": [
                            {'activation_indent': 0.6, 'offset_indent': 0.01},
                            {'activation_indent': 1.2, 'offset_indent': 0.6}, 
                            {'activation_indent': 1.8, 'offset_indent': 1.2}, 
                            {'activation_indent': 2.4, 'offset_indent': 1.8}, 
                            {'activation_indent': 3.0, 'offset_indent': 2.4}, 
                            {'activation_indent': 3.6, 'offset_indent': 3.0},
                            {'activation_indent': 4.4, 'offset_indent': 3.6},
                            {'activation_indent': 4.8, 'offset_indent': 4.4},
                            {'activation_indent': 5.4, 'offset_indent': 4.8}, 
                            {'activation_indent': 6.0, 'offset_indent': 5.4},                       
                        ]
                    } 
                }
            },

            "SHORT": {
                "entry_conditions": {
                    "rules": {
                        'CRON': {
                            'enable': True,            # True/False -- использовать/не использовать
                            'tfr': "5m",
                            'period': 0,
                            "ind_name": 'CRON_IND'
                        },  #               
                    },     
                    "is_close_bar": True,       # Дожидаться закрытия бара                
                    "grid_orders": [
                        {'indent': 0.0, 'volume': 14, 'signal': True},
                        {'indent': -3.0, 'volume': 14, 'signal': False}, # %
                        {'indent': -9.0, 'volume': 14, 'signal': False}, # %
                        {'indent': -27.0, 'volume': 14, 'signal': False}, # %
                        {'indent': -81.0, 'volume': 14, 'signal': False}, # %
                        {'indent': -243.0, 'volume': 14, 'signal': False}, # %
                    ],                     
                },

                "exit_conditions": {                              
                    "close_by_signal": {
                        "is_active": False,    # Закрытие по сигналу
                        "min_profit": 0.6,   # Минимальный профит при закрытии по сигналу. None -- откл
                    },  
                    "trailing_sl": {
                        "enable": False,
                        "is_move_tp": True,
                        "val": [
                            {'activation_indent': 0.6, 'offset_indent': 0.01},
                            {'activation_indent': 1.2, 'offset_indent': 0.6}, 
                            {'activation_indent': 1.8, 'offset_indent': 1.2}, 
                            {'activation_indent': 2.4, 'offset_indent': 1.8}, 
                            {'activation_indent': 3.0, 'offset_indent': 2.4}, 
                            {'activation_indent': 3.6, 'offset_indent': 3.0},
                            {'activation_indent': 4.4, 'offset_indent': 3.6},
                            {'activation_indent': 4.8, 'offset_indent': 4.4},
                            {'activation_indent': 5.4, 'offset_indent': 4.8}, 
                            {'activation_indent': 6.0, 'offset_indent': 5.4},                       
                        ]
                    } 
                }
            }                        
        }),
    ]
